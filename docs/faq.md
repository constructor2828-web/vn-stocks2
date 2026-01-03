---
layout: default
title: FAQ
---

# Frequently Asked Questions ❓

Common questions and answers about GSC Stock Exchange.

---

## Getting Started

### How do I start trading?

Type `/register` in Discord to create your account. You'll receive 10 Cogs starting capital automatically.

### Can I register more than once?

No, each Discord account can only register once. Your account and balance are permanent.

### What if I lose all my money?

Contact an admin - they might give you a small bailout to get back on your feet! Or wait for giveaways and events.

---

## Money & Pricing

### What are Cogs and Spurs?

**Cogs** are the main currency (like dollars). **Spurs** are fractional units (like cents).
- 1 Cog = 64 Spurs
- All prices shown in Cogs
- Bot handles conversion automatically

### Why 64 Spurs per Cog?

It's based on Minecraft's stack system (64 items per stack) and fits the server's lore!

### How are prices calculated?

Every 3 minutes, prices update based on:
- **Team activity** (40%) - Discord messages from team members
- **Random volatility** (30%) - Natural market noise
- **Momentum** (20%) - Trend persistence
- **Mean reversion** (10%) - Price corrections

### Can prices go negative?

No, prices have a minimum floor to prevent going below zero.

### Why did a stock price suddenly spike/crash?

Could be:
- High team activity in Discord
- Random volatility (especially for VIOL/CRAV)
- Momentum from existing trend
- Multiple traders buying/selling

---

## Trading

### How do I know when to buy or sell?

**Buy signals:**
- Price dropped significantly (10%+)
- Team activity is ramping up
- Candlestick chart shows reversal pattern

**Sell signals:**
- You've made good profit (20%+)
- Price spiked unusually high
- Team activity is dying down

See the [Trading Guide](trading.html) for detailed strategies!

### What's the best stock to buy?

There's no "best" stock - each has pros and cons:
- **High volatility** (VIOL/CRAV) - Bigger gains but riskier
- **Low volatility** (ROSE/VOC) - Safer but smaller gains
- **Active teams** - More price movement

Diversify across multiple stocks!

### Can I lose more money than I have?

No, you can only buy what you can afford. The bot prevents overdrafts.

### Why can't I sell my stocks?

Check:
- Do you actually own those shares? (Use `/portfolio`)
- Are you typing the symbol correctly?
- Did you already place a sell limit order for them?

### Do I pay fees or commissions?

No! All trades are commission-free. Buy/sell at market price with no extra costs.

---

## Limit Orders

### What happens if my limit order never triggers?

Orders expire after **24 hours** automatically. You can create a new one if still interested.

### Can I edit a limit order?

No, you must cancel it (`/cancelorder`) and create a new one.

### Why did my limit order cancel automatically?

Possible reasons:
- Order expired (24 hour limit)
- You sold the shares manually (for sell orders)
- Admin reset the market
- Insufficient balance at execution time

### Do limit orders cost anything to create?

**Buy orders:** Money is reserved when created
**Sell orders:** Shares must be in portfolio
No fees for creating/canceling orders!

### What if multiple people have orders at the same price?

First come, first served - whoever placed their order earlier gets filled first.

---

## Price Alerts

### How often are alerts checked?

Every **60 seconds**, the bot scans all prices and triggers matching alerts.

### Why didn't I get an alert?

Check:
- Are DMs enabled for this server?
- Did you set the alert direction correctly (above/below)?
- Did the price actually cross your threshold?
- Alert triggers once then deletes - already triggered?

### Can I reuse an alert?

No, alerts are one-time use. After triggering, they auto-delete. Create a new one if needed.

### How many alerts can I have?

Unlimited! Set as many as you want.

---

## Charts & Analysis

### What do the graph colors mean?

**TradingView style:**
- **Green line** - Price is above starting point
- **Red line** - Price is below starting point
- **Dark background** - Easier on the eyes
- **Grid lines** - Help read exact values

### What are candlestick charts?

Each "candle" shows price movement over one hour:
- **Green candle** - Price went up
- **Red candle** - Price went down
- **Wick** - Shows highest/lowest prices
- **Body** - Shows open/close prices

See [Advanced Features](advanced.html#candlestick-charts) for details!

### Why does the graph show "no data"?

Stock might be brand new with limited price history. Wait a few hours for data to accumulate.

### Can I see historical data from weeks ago?

Yes! Use `/candlestick symbol:STMP period:30d` for last 30 days of data.

---

## Portfolio & Performance

### How is profit/loss calculated?

**For each stock:**
```
P/L = (Current Price × Shares) - (Average Buy Price × Shares)
```

**Total P/L:**
```
Total = (Cash + Portfolio Value) - Starting Capital (10 Cogs)
```

### What does ROI mean?

**Return on Investment** - percentage gain or loss:
```
ROI = (Profit / Investment) × 100%
```

Example: Invested 100 Cogs, now worth 125 Cogs = +25% ROI

### Why is my portfolio value different from my purchases?

Prices change! Your portfolio value is based on **current market prices**, not what you paid.

### Does the pie chart update automatically?

No, run `/portfolio` again to refresh. Each chart is a snapshot at that moment.

---

## Achievements

### How do I earn achievements?

Achievements unlock automatically when you meet the criteria. No need to claim them!

### Can I lose achievements?

No, once earned they're permanent badges!

### What's the rarest achievement?

**🌟 Moon Mission** (Legendary) - Requires 1000%+ profit on a single trade. Extremely difficult!

### Do achievements give rewards?

They're purely for bragging rights and showing your trading skill!

---

## Technical Issues

### Bot isn't responding to commands

Check:
- Is the bot online? (Should show green status)
- Are you in the right Discord server?
- Did you spell the command correctly? (Use `/` to see autocomplete)

### "This interaction failed" error

Usually means:
- Bot lagged (try again)
- Invalid parameters (check symbol names, numbers)
- Database timeout (rare, try again)

### Graphs not displaying

Make sure:
- Discord can display embeds/images
- Your internet connection is stable
- Graph command has all required parameters

### Lost all my data!

Don't panic - data is stored in database. Contact an admin, they can check/restore.

---

## Strategy Questions

### What's the best strategy for beginners?

**Activity trading:**
1. Watch Discord channels
2. Buy stocks when teams are super active
3. Sell after a few updates when activity dies
4. Repeat!

Simple and effective. See [Trading Guide](trading.html) for more!

### Should I buy and hold or day trade?

**Buy and hold (long-term):**
- Less stressful
- Safer, steadier gains
- Good for busy people

**Day trading (short-term):**
- More active, more exciting
- Can make quick profits
- Requires constant monitoring

Try both and see what fits your style!

### How much should I invest in each stock?

**Safe approach:**
- 20-25% per stock
- Hold 4-5 different stocks
- Keep 15-20% cash

**Aggressive approach:**
- 30-40% per stock
- Hold 2-3 stocks
- Keep 10% cash

Never put 100% in one stock!

### When should I use limit orders vs manual trading?

**Limit orders:**
- You have a specific target price
- You can't watch charts 24/7
- You want to remove emotion

**Manual trading:**
- Price is good right now
- Market conditions changing rapidly
- You want immediate execution

Use both together!

---

## Market Mechanics

### Why do some teams have higher volatility?

It's part of their configuration - reflects team characteristics:
- **High volatility** - More chaotic, unpredictable teams
- **Low volatility** - Stable, consistent teams

Volatility can't be changed.

### Does selling affect the price?

No, individual trades don't move the market. Prices only change during 3-minute update cycles based on activity and algorithms.

### What happens during market updates?

Every 3 minutes:
1. Bot checks Discord activity for each team
2. Calculates new prices using the formula
3. Updates all stock prices
4. Executes any triggered limit orders
5. Checks price alerts
6. Records prices in history

### Can admins manipulate prices?

Yes, admins can use `/setprice` for manual adjustments, but it's logged. Used mainly for bug fixes or special events.

---

## Still Have Questions?

Check these resources:
- [🏠 Home](index.html) - Overview and quick links
- [📖 Getting Started](getting-started.html) - Basics tutorial
- [📈 Trading Guide](trading.html) - Strategies and tips
- [⚡ Advanced Features](advanced.html) - Limit orders, alerts, etc.
- [📋 Commands](commands.html) - Full command reference

Or ask in the Discord server - traders love helping newcomers!

---

<div class="info-box success">
<strong>Happy Trading! 🎯</strong><br>
Remember: the best way to learn is by doing. Start small, experiment, and have fun!
</div>
