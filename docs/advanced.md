---
layout: default
title: Advanced Features
---

# Advanced Features ⚡

Take your trading to the next level with powerful automation and analysis tools.

---

## Limit Orders 🎯

### What Are Limit Orders?

Limit orders let you set automatic buy/sell orders that execute when prices hit your target - even while you're offline!

**Benefits:**
- Trade 24/7 without watching charts
- Never miss perfect entry/exit points
- Remove emotion from trading decisions
- Secure profits automatically

### Creating Limit Buy Orders

Buy stocks automatically when price drops to your target.

<div class="command-example">
<div class="command">/limitbuy symbol:STMP shares:10 price:18</div>
<div class="description">Buys 10 STMP shares if price drops to 18 Cogs or lower</div>
</div>

**Real-world scenario:**
```
Current situation:
- STMP trading at 22 Cogs (too expensive for you)
- You want to buy at 18 Cogs (good value)
- You're going to bed soon

Action:
/limitbuy symbol:STMP shares:10 price:18

What happens:
- Order sits waiting (shows in /orders)
- Overnight, STMP drops to 17.8 Cogs
- Order executes automatically!
- You wake up owning 10 STMP at 17.8 Cogs
- Cost: 178 Cogs deducted from balance
```

<div class="info-box success">
<strong>Pro Tip:</strong> Set limit buys 10-15% below current price to catch dips
</div>

### Creating Limit Sell Orders

Sell stocks automatically when price rises to your target.

<div class="command-example">
<div class="command">/limitsell symbol:VIOL shares:15 price:25</div>
<div class="description">Sells 15 VIOL shares if price rises to 25 Cogs or higher</div>
</div>

**Real-world scenario:**
```
Current situation:
- You own 15 VIOL bought at 18 Cogs
- VIOL currently at 20 Cogs
- You want to sell at 25 Cogs (39% profit)
- You'll be at work all day

Action:
/limitsell symbol:VIOL shares:15 price:25

What happens:
- Order waits in queue
- During the day, VIOL spikes to 25.4 Cogs
- Order executes at 25 Cogs!
- You get 375 Cogs (15 × 25)
- Profit: 105 Cogs (+39%) secured
```

<div class="info-box tip">
<strong>Strategy:</strong> Use limit sells to lock in 20-30% profits automatically
</div>

### Managing Your Orders

View all active limit orders:

<div class="command-example">
<div class="command">/orders</div>
<div class="description">Lists all pending limit orders with details</div>
</div>

**Example output:**
```
📋 Your Active Limit Orders
━━━━━━━━━━━━━━━━━━━━━━━━━━

Order #1 (Buy)
Symbol: STMP
Shares: 10
Target Price: 18 Cogs
Current Price: 22 Cogs
Status: Waiting (needs -18% drop)
Expires: Jan 5, 2026 10:30 AM

Order #2 (Sell)
Symbol: VIOL
Shares: 15
Target Price: 25 Cogs
Current Price: 20 Cogs
Status: Waiting (needs +25% rise)
Expires: Jan 4, 2026 3:15 PM
```

Cancel an order:

<div class="command-example">
<div class="command">/cancelorder order_id:1</div>
<div class="description">Cancels order #1 (get ID from /orders)</div>
</div>

### Limit Order Rules ⚠️

**Expiration:** All orders expire after **24 hours**

**Why:** Prevents old orders from executing at bad prices

**What happens:** Expired orders auto-delete, you get notified

**Balance requirements:**
- **Buy orders:** Money reserved when order created
- **Sell orders:** Shares must be in portfolio
- If you sell shares manually, sell limit orders cancel

**Execution order:**
- Multiple orders at same price = first come, first served
- Orders execute during market updates (every 3 minutes)
- You get DM notification when order fills

**Limits:**
- Maximum **10 active orders** per user
- Can't have duplicate orders (same stock/price/type)

---

## Price Alerts 🔔

### What Are Price Alerts?

Get instant Discord DM when a stock hits your target price - no need to watch charts!

**Benefits:**
- Never miss important price levels
- Monitor multiple stocks simultaneously
- Perfect for busy traders
- Catch opportunities while offline

### Setting Alerts Above Current Price

Get notified when price goes up:

<div class="command-example">
<div class="command">/alert symbol:CRAV type:above price:30</div>
<div class="description">DMs you when CRAV price rises above 30 Cogs</div>
</div>

**Use case - Sell signal:**
```
Situation:
- You own 20 CRAV bought at 25 Cogs
- Want to sell at 30 Cogs (+20% profit)
- Don't want to check price every hour

Action:
/alert symbol:CRAV type:above price:30

Result:
- CRAV price hits 30.2 Cogs
- Bot DMs you: "🔔 CRAV is now 30.2 Cogs (above your 30 Cogs alert)"
- You quickly /sell symbol:CRAV shares:20
- Profit secured!
```

### Setting Alerts Below Current Price

Get notified when price goes down:

<div class="command-example">
<div class="command">/alert symbol:ROSE type:below price:12</div>
<div class="description">DMs you when ROSE price drops below 12 Cogs</div>
</div>

**Use case - Buy signal:**
```
Situation:
- ROSE currently at 15 Cogs
- You think 12 Cogs is great value
- Waiting for a dip to buy

Action:
/alert symbol:ROSE type:below price:12

Result:
- Market correction, ROSE drops to 11.8 Cogs
- Bot DMs you: "🔔 ROSE is now 11.8 Cogs (below your 12 Cogs alert)"
- You buy 30 shares at discount
- Later sell at 14 Cogs for +18% profit
```

### Managing Alerts

View all active alerts:

<div class="command-example">
<div class="command">/alerts</div>
<div class="description">Lists all your price alerts</div>
</div>

**Example output:**
```
🔔 Your Price Alerts
━━━━━━━━━━━━━━━━━━━━

Alert #1
Symbol: CRAV
Target: Above 30 Cogs
Current: 27.5 Cogs
Status: Monitoring

Alert #2
Symbol: ROSE
Target: Below 12 Cogs
Current: 15 Cogs
Status: Monitoring

Alert #3
Symbol: STMP
Target: Above 25 Cogs
Current: 22 Cogs
Status: Monitoring
```

Remove an alert:

<div class="command-example">
<div class="command">/removealert alert_id:1</div>
<div class="description">Removes alert #1 (get ID from /alerts)</div>
</div>

### Alert Behavior 🎯

**One-time use:** Alerts trigger once, then auto-delete

**Why:** Prevents spam and ensures relevance

**Checking frequency:** Every 60 seconds

**Instant notifications:** DM sent immediately when price hits

**No limits:** Set as many alerts as you want!

### Alert Strategies

**Breakout alerts:**
```
Stock consolidating at 20 Cogs
Set alert above 22 Cogs (breakout level)
When triggered → momentum trade
```

**Support alerts:**
```
Stock has support at 18 Cogs
Set alert below 17 Cogs (breakdown)
When triggered → sell/avoid
```

**Mean reversion alerts:**
```
Stock normally 15-17 Cogs
Set alert below 14 Cogs (oversold)
When triggered → buy the dip
```

---

## Watchlist 👀

### What Is a Watchlist?

Track stocks you're interested in without owning them - see price changes at a glance.

**Benefits:**
- Monitor potential buys
- Track competitors
- See sector trends
- Quick price overview

### Adding Stocks to Watchlist

<div class="command-example">
<div class="command">/watch symbol:POT</div>
<div class="description">Adds POT to your watchlist</div>
</div>

### Viewing Your Watchlist

<div class="command-example">
<div class="command">/watchlist</div>
<div class="description">Shows all watched stocks with 24h changes</div>
</div>

**Example output:**
```
👀 Your Watchlist
━━━━━━━━━━━━━━━━━━━━

POT: 12.45 Cogs (+3.2%)
STMP: 20.87 Cogs (-1.5%)
CRAV: 28.12 Cogs (+5.7%)
VIOL: 19.03 Cogs (+2.1%)

💰 Cash Available: 125 Cogs
```

### Removing from Watchlist

<div class="command-example">
<div class="command">/unwatch symbol:POT</div>
<div class="description">Removes POT from watchlist</div>
</div>

**Limits:** Maximum **10 stocks** on watchlist

---

## Trade History 📜

### Viewing Your Trades

See all past transactions with P/L calculations:

<div class="command-example">
<div class="command">/history</div>
<div class="description">Shows recent transaction history</div>
</div>

**Example output:**
```
📜 Trading History
━━━━━━━━━━━━━━━━━━━━

Jan 3, 10:45 AM
SOLD 10 STMP @ 22.5 Cogs
Total: 225 Cogs
P/L: +25 Cogs (+12.5%)

Jan 3, 9:30 AM
BOUGHT 10 STMP @ 20 Cogs
Total: 200 Cogs

Jan 2, 3:15 PM
SOLD 15 VIOL @ 21 Cogs
Total: 315 Cogs
P/L: +45 Cogs (+16.7%)
```

### Filtering History

View trades for specific stock:

<div class="command-example">
<div class="command">/history symbol:STMP</div>
<div class="description">Shows only STMP trades</div>
</div>

---

## Portfolio Analytics 📊

### Advanced Portfolio View

<div class="command-example">
<div class="command">/portfolio</div>
<div class="description">Shows detailed holdings with pie chart</div>
</div>

**What you get:**
- **Holdings breakdown:** Each stock's current value
- **Profit/Loss:** Per position and total
- **ROI percentage:** Return on investment
- **Asset allocation:** Visual pie chart
- **Total net worth:** Cash + holdings

**Example output:**
```
📊 Portfolio Analytics
━━━━━━━━━━━━━━━━━━━━

Holdings:
━━━━━━━━
STMP: 10 shares @ 22.5 Cogs
  Current Value: 225 Cogs
  Cost Basis: 200 Cogs
  P/L: +25 Cogs (+12.5%)
  
VIOL: 5 shares @ 19.8 Cogs
  Current Value: 99 Cogs
  Cost Basis: 90 Cogs
  P/L: +9 Cogs (+10%)

Summary:
━━━━━━━━
Cash: 76 Cogs
Holdings: 324 Cogs
Total Worth: 400 Cogs

Overall P/L: +110 Cogs (+37.9%)
```

Plus a pie chart showing allocation!

---

## Candlestick Charts 📉

### What Are Candlestick Charts?

Professional-grade OHLC (Open-High-Low-Close) charts showing price patterns.

<div class="command-example">
<div class="command">/candlestick symbol:STMP period:24h</div>
<div class="description">Shows hourly candlesticks for last 24 hours</div>
</div>

**What you see:**
- **Green candles:** Price went up that hour
- **Red candles:** Price went down
- **Wicks:** Show high/low extremes
- **Body:** Shows open/close prices

**Available periods:**
- `24h` - Last 24 hours (hourly candles)
- `7d` - Last 7 days (daily candles)
- `30d` - Last 30 days (daily candles)

### Reading Candles

**Bullish patterns (buy signals):**
- Multiple green candles in a row
- Long green candles (strong buying)
- Small red candles after big drop (reversal)

**Bearish patterns (sell signals):**
- Multiple red candles in a row
- Long red candles (strong selling)
- Small green candles after big rise (exhaustion)

<div class="info-box tip">
<strong>Pro Tip:</strong> Use candlesticks with <code>/graph</code> for complete technical analysis
</div>

---

## Achievements System 🏆

### Earning Badges

Unlock rare achievements by trading and reaching milestones!

<div class="command-example">
<div class="command">/achievements</div>
<div class="description">Shows all achievements and your progress</div>
</div>

### Achievement List

**Common (Easy to get):**
- 🎯 **First Trade** - Complete your first transaction
- 💰 **Profit Taker** - Make 50+ Cogs profit on a trade

**Uncommon (Medium difficulty):**
- 💎 **Diamond Hands** - Hold a stock for 7+ days
- 📈 **Bull Market** - Earn 100+ Cogs total profit
- 🏆 **Millionaire** - Reach 100 Cogs net worth

**Rare (Challenging):**
- 🐋 **Whale** - Own 1000+ total shares
- 🎰 **High Roller** - Complete 100+ trades
- 📊 **Diversified** - Own shares in 5+ different stocks

**Epic (Very hard):**
- 🔥 **Hot Streak** - Win 10 profitable trades in a row
- 👑 **Market Leader** - Reach #1 on leaderboard

**Legendary (Extremely rare):**
- 🌟 **Moon Mission** - 1000%+ profit on a single trade

<div class="info-box success">
<strong>Bragging rights!</strong> Show off your achievements in Discord
</div>

---

## Tips for Power Users

### Combine Tools for Maximum Effect

**Example workflow:**
```
1. Add stocks to watchlist (/watch)
2. Set price alerts for buy points (/alert type:below)
3. When alerted, check /candlestick for confirmation
4. Place limit buy orders (/limitbuy)
5. Set sell limit orders for profit targets (/limitsell)
6. Monitor with /portfolio pie charts
7. Track performance in /history
```

### Automation Setup

**While you sleep:**
```
/limitbuy symbol:ROSE shares:20 price:13
/limitsell symbol:STMP shares:15 price:25
/alert symbol:CRAV type:above price:30
```

All three work 24/7 automatically!

### Daily Routine

**Morning:**
1. Check `/watchlist` for overnight changes
2. Review `/alerts` for any triggers
3. Check `/orders` for executed limit orders
4. Plan day's trades based on data

**Evening:**
1. Set limit orders for overnight execution
2. Create alerts for key price levels
3. Review `/portfolio` for P/L
4. Check `/history` for completed trades

---

## Next Steps

- [📋 Full Command Reference](commands.html) - All commands explained
- [❓ FAQ](faq.html) - Common questions
- [🏠 Back to Home](index.html)

<div class="info-box success">
<strong>You're now a GSC pro!</strong><br>
Use these advanced tools to trade smarter, not harder. Automation and analytics give you an edge over manual traders!
</div>
