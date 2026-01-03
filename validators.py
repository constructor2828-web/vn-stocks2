"""Input validation and sanitization utilities."""
import re
from typing import Optional
from logger import logger

# Maximum limits to prevent integer overflow and abuse
MAX_SHARES = 1_000_000
MAX_PRICE = 1_000_000_000  # 1 billion spurs
MAX_SYMBOL_LENGTH = 10
MAX_BALANCE = 10_000_000_000  # 10 billion spurs


def validate_symbol(symbol: str) -> bool:
    """
    Validate stock symbol is alphanumeric and reasonable length.
    
    Args:
        symbol: Stock symbol to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not symbol:
        return False
    
    if len(symbol) > MAX_SYMBOL_LENGTH:
        logger.warning(f"Symbol too long: {symbol}")
        return False
    
    if not symbol.isalnum():
        logger.warning(f"Symbol contains invalid characters: {symbol}")
        return False
    
    return True


def sanitize_symbol(symbol: str) -> str:
    """
    Sanitize symbol by removing invalid characters.
    
    Args:
        symbol: Raw symbol input
        
    Returns:
        Sanitized symbol (uppercase, alphanumeric only)
    """
    # Remove all non-alphanumeric characters
    sanitized = re.sub(r'[^A-Za-z0-9]', '', symbol)
    
    # Convert to uppercase
    sanitized = sanitized.upper()
    
    # Limit length
    sanitized = sanitized[:MAX_SYMBOL_LENGTH]
    
    return sanitized


def validate_shares(shares: int) -> tuple[bool, Optional[str]]:
    """
    Validate share count is positive and within limits.
    
    Args:
        shares: Number of shares
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if shares <= 0:
        return False, "Number of shares must be positive"
    
    if shares > MAX_SHARES:
        return False, f"Number of shares exceeds maximum ({MAX_SHARES:,})"
    
    return True, None


def validate_price(price: int) -> tuple[bool, Optional[str]]:
    """
    Validate price is positive and within limits.
    
    Args:
        price: Price in spurs
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if price <= 0:
        return False, "Price must be positive"
    
    if price > MAX_PRICE:
        return False, f"Price exceeds maximum ({MAX_PRICE:,} spurs)"
    
    return True, None


def validate_balance(balance: int) -> tuple[bool, Optional[str]]:
    """
    Validate balance is within safe limits.
    
    Args:
        balance: Balance in spurs
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if balance < 0:
        return False, "Balance cannot be negative"
    
    if balance > MAX_BALANCE:
        return False, f"Balance exceeds maximum ({MAX_BALANCE:,} spurs)"
    
    return True, None


def validate_transaction(shares: int, price: int) -> tuple[bool, Optional[str]]:
    """
    Validate a transaction's shares and price don't cause overflow.
    
    Args:
        shares: Number of shares
        price: Price per share in spurs
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check individual values
    valid_shares, shares_error = validate_shares(shares)
    if not valid_shares:
        return False, shares_error
    
    valid_price, price_error = validate_price(price)
    if not valid_price:
        return False, price_error
    
    # Check multiplication won't overflow
    total_cost = shares * price
    if total_cost > MAX_BALANCE:
        return False, f"Transaction total ({total_cost:,}) exceeds maximum"
    
    return True, None


def validate_filepath(filepath: str, base_dir: str) -> bool:
    """
    Validate filepath doesn't attempt directory traversal.
    
    Args:
        filepath: Path to validate
        base_dir: Base directory that should contain the file
        
    Returns:
        True if safe, False if potential security risk
    """
    import os
    
    # Resolve to absolute paths
    abs_filepath = os.path.abspath(filepath)
    abs_base_dir = os.path.abspath(base_dir)
    
    # Check if filepath is within base_dir
    if not abs_filepath.startswith(abs_base_dir):
        logger.warning(f"Path traversal attempt detected: {filepath}")
        return False
    
    return True
