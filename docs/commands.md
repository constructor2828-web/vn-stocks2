---
layout: default
title: Commands Reference
---

# Commands Reference 📋

Complete list of all available commands in GSC.

---

## Basic Commands 🎯

### Account Management

<div class="command-example">
<div class="command">/register</div>
<div class="description">Create your trading account and receive 10 Cogs starting capital</div>
</div>

<div class="command-example">
<div class="command">/balance</div>
<div class="description">Check your current cash balance and portfolio value</div>
</div>

### Trading

<div class="command-example">
<div class="command">/buy symbol:[SYMBOL] shares:[NUMBER]</div>
<div class="description">Buy shares at current market price<br>
Example: <code>/buy symbol:STMP shares:10</code></div>
</div>

<div class="command-example">
<div class="command">/sell symbol:[SYMBOL] shares:[NUMBER]</div>
<div class="description">Sell shares at current market price<br>
Example: <code>/sell symbol:VIOL shares:5</code></div>
</div>

---

## Market Information 📊

<div class="command-example">
<div class="command">/market</div>
<div class="description">View all available stocks with current prices and 24h changes</div>
</div>

<div class="command-example">
<div class="command">/stock symbol:[SYMBOL]</div>
<div class="description">Get detailed information about a specific stock<br>
Example: <code>/stock symbol:CRAV</code></div>
</div>

<div class="command-example">
<div class="command">/leaderboard</div>
<div class="description">See top 10 richest traders by total net worth</div>
</div>

---

## Charts & Analysis 📈

<div class="command-example">
<div class="command">/graph symbol:[SYMBOL]</div>
<div class="description">Display live-updating line chart with TradingView styling<br>
Updates every 30 seconds, auto-stops after 120s inactivity<br>
Example: <code>/graph symbol:STMP</code></div>
</div>

<div class="command-example">
<div class="command">/candlestick symbol:[SYMBOL] period:[24h|7d|30d]</div>
<div class="description">Show OHLC candlestick chart<br>
Example: <code>/candlestick symbol:ROSE period:24h</code></div>
</div>

<div class="command-example">
<div class="command">/portfolio</div>
<div class="description">View your holdings with P/L tracking and pie chart visualization</div>
</div>

---

## Limit Orders ⚡

<div class="command-example">
<div class="command">/limitbuy symbol:[SYMBOL] shares:[NUMBER] price:[PRICE]</div>
<div class="description">Create automatic buy order at target price<br>
Example: <code>/limitbuy symbol:POT shares:20 price:11</code></div>
</div>

<div class="command-example">
<div class="command">/limitsell symbol:[SYMBOL] shares:[NUMBER] price:[PRICE]</div>
<div class="description">Create automatic sell order at target price<br>
Example: <code>/limitsell symbol:VIOL shares:15 price:25</code></div>
</div>

<div class="command-example">
<div class="command">/orders</div>
<div class="description">List all your active limit orders with details</div>
</div>

<div class="command-example">
<div class="command">/cancelorder order_id:[ID]</div>
<div class="description">Cancel a specific limit order<br>
Example: <code>/cancelorder order_id:1</code></div>
</div>

---

## Price Alerts 🔔

<div class="command-example">
<div class="command">/alert symbol:[SYMBOL] type:[above|below] price:[PRICE]</div>
<div class="description">Set price alert for DM notification<br>
Example: <code>/alert symbol:CRAV type:above price:30</code></div>
</div>

<div class="command-example">
<div class="command">/alerts</div>
<div class="description">View all your active price alerts</div>
</div>

<div class="command-example">
<div class="command">/removealert alert_id:[ID]</div>
<div class="description">Remove a specific price alert<br>
Example: <code>/removealert alert_id:1</code></div>
</div>

---

## Tracking & History 📜

<div class="command-example">
<div class="command">/history [symbol:SYMBOL]</div>
<div class="description">View your trade history with P/L calculations<br>
Optional: Filter by symbol<br>
Example: <code>/history symbol:STMP</code></div>
</div>

<div class="command-example">
<div class="command">/watch symbol:[SYMBOL]</div>
<div class="description">Add stock to watchlist (max 10)<br>
Example: <code>/watch symbol:POT</code></div>
</div>

<div class="command-example">
<div class="command">/unwatch symbol:[SYMBOL]</div>
<div class="description">Remove stock from watchlist<br>
Example: <code>/unwatch symbol:POT</code></div>
</div>

<div class="command-example">
<div class="command">/watchlist</div>
<div class="description">View all watched stocks with 24h price changes</div>
</div>

---

## Achievements 🏆

<div class="command-example">
<div class="command">/achievements</div>
<div class="description">View all available achievements and your progress</div>
</div>

---

## Information & Help ℹ️

<div class="command-example">
<div class="command">/help</div>
<div class="description">Display comprehensive help message with command categories</div>
</div>

<div class="command-example">
<div class="command">/activity</div>
<div class="description">Show current market activity by team (message counts)</div>
</div>

---

## Admin Commands 👑

**(Requires Admin role)**

<div class="command-example">
<div class="command">/give user:[USER] amount:[AMOUNT]</div>
<div class="description">Give money to a player<br>
Example: <code>/give user:@Player amount:50</code></div>
</div>

<div class="command-example">
<div class="command">/setprice symbol:[SYMBOL] price:[PRICE]</div>
<div class="description">Manually set stock price<br>
Example: <code>/setprice symbol:STMP price:20</code></div>
</div>

<div class="command-example">
<div class="command">/resetmarket</div>
<div class="description">Reset all stock prices to starting values (DANGEROUS)</div>
</div>

---

## Quick Reference Table

| Category | Commands | Purpose |
|----------|----------|---------|
| **Setup** | `/register`, `/balance` | Account creation |
| **Trading** | `/buy`, `/sell` | Basic transactions |
| **Market** | `/market`, `/stock`, `/leaderboard` | Price info |
| **Charts** | `/graph`, `/candlestick`, `/portfolio` | Visualization |
| **Automation** | `/limitbuy`, `/limitsell`, `/orders` | Limit orders |
| **Alerts** | `/alert`, `/alerts`, `/removealert` | Price notifications |
| **Tracking** | `/history`, `/watch`, `/watchlist` | Monitoring |
| **Progress** | `/achievements` | Badges |
| **Help** | `/help`, `/activity` | Information |
| **Admin** | `/give`, `/setprice`, `/resetmarket` | Management |

---

## Command Tips 💡

### Stock Symbols
All commands use these symbols:
- `STMP` - Steamporium
- `ROSE` - Rosebud
- `VIOL` - Violetvale
- `POT` - Potpourri
- `CRAV` - Cravat
- `VOC` - Voco

### Price Format
- Prices always in **Cogs** (e.g., `15.75`)
- Bot handles Spur conversion automatically
- Supports decimals for precise pricing

### Common Workflows

**Check then buy:**
```
/market → /stock symbol:STMP → /buy symbol:STMP shares:10
```

**Monitor then alert:**
```
/watch symbol:VIOL → /alert symbol:VIOL type:above price:25
```

**Analyze then trade:**
```
/graph symbol:CRAV → /candlestick symbol:CRAV period:24h → /buy
```

---

## Next Steps

- [🏠 Back to Home](index.html)
- [📖 Getting Started Guide](getting-started.html)
- [📈 Trading Strategies](trading.html)
- [⚡ Advanced Features](advanced.html)
- [❓ FAQ](faq.html)

<div class="info-box tip">
<strong>Bookmark this page!</strong><br>
Use it as your quick reference guide while trading in Discord.
</div>
