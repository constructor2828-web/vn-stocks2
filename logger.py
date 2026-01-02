"""Centralized logging configuration for the bot."""
import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging format
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Create logger
logger = logging.getLogger('economy_bot')
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

# File handler (daily log rotation)
log_filename = os.path.join(LOG_DIR, f'bot_{datetime.utcnow().strftime("%Y%m%d")}.log')
file_handler = logging.FileHandler(log_filename, encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Prevent propagation to root logger
logger.propagate = False
