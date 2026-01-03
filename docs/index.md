# GSC Stock Exchange - Player Guide

Welcome to the Gearfall Stock Exchange! This is your guide to trading team stocks and building your fortune.

## 🎮 Getting Started

### What is GSC?
GSC is a stock market simulator where you trade stocks based on team performance. Prices change every 3 minutes based on activity, volatility, and momentum.

### First Steps
1. **Register**: Use `/register` to create your trading account
2. **Check Balance**: Use `/balance` to see you start with 10 Cogs
3. **View Market**: Use `/market` to see all available stocks
4. **Start Trading**: Use `/buy` or `/sell` to make your first trade!

---

## 💰 Understanding Money

### Currency System
- **1 Cog = 64 Spurs**
- You start with **10 Cogs** (640 Spurs)
- All prices shown in Cogs for simplicity
- Bot handles conversion automatically

### Example
- Stock price: 15.5 Cogs
- Buy 10 shares = 155 Cogs total
- Sell 5 shares = 77.5 Cogs back

---

## 📈 How Trading Works

### Buying Stocks
```
/buy STMP 10
```
This buys 10 shares of Team Steampire stock at current price.

**Before buying, make sure:**
- You have enough Cogs
- You checked the current price with `/stock STMP`
- You're not buying your own team (anti-manipulation rule)

### Selling Stocks
```
/sell ROSE 5
```
This sells 5 shares of Team Rose stock.

**You can only sell what you own!** Check `/portfolio` first.

### Quick Trading
Use `/stock STMP` to get an interactive button menu for quick trades!

---

## 📊 Market Basics

### Available Teams
- **STMP** - Team Steampire
- **VOC** - Team VOC
- **CRAV** - Team Crava
- **ROSE** - Team Rose
- **VIOL** - Team Violet
- **POT** - Team Potchi

### What Affects Prices?
1. **Team Activity**: More messages = higher prices
2. **Volatility**: Random market movements
3. **Momentum**: Stocks on a trend continue moving
4. **Time**: Prices update every 3 minutes

### Reading Price Changes
- 📈 **Green/Up**: Price increased
- 📉 **Red/Down**: Price decreased
- **Percentage**: How much it changed (e.g., +5.2%)

---

## 🎯 Advanced Features

### Limit Orders
Set orders that trigger automatically when price hits your target:
- `/limitbuy STMP 10 12.5` - Buy 10 shares when price drops to 12.5
- `/limitsell ROSE 5 20` - Sell 5 shares when price rises to 20
- `/orders` - View your active orders
- `/cancelorder 123` - Cancel order #123

**Why use limit orders?**
- Don't need to watch market 24/7
- Catch good prices while you sleep
- Auto-execute at your target price

### Price Alerts
Get DM'd when stocks hit your targets:
- `/alert CRAV above 25` - Alert when CRAV goes above 25
- `/alert VIOL below 15` - Alert when VIOL drops below 15
- `/alerts` - View your alerts
- `/removealert 5` - Delete alert #5

**Tip**: Set alerts for prices you're watching, then decide whether to trade!

### Watchlist
Track stocks without buying them:
- `/watch POT` - Add POT to watchlist
- `/watchlist` - See all watched stocks with 24h changes
- `/unwatch POT` - Remove from watchlist

**Great for**: Researching before buying, tracking competitors

---

## 📱 Useful Commands

### Portfolio Management
- `/portfolio` - See your holdings with pie chart and P/L
- `/balance` - Check your cash balance
- `/history 7` - View last 7 days of trades
- `/history 7 STMP` - View STMP trades only

### Market Analysis
- `/market` - All stock prices
- `/stock STMP` - Detailed info about STMP
- `/graph STMP` - Price history chart (live updating!)
- `/candlestick STMP` - Professional OHLC chart
- `/leaderboard` - Top traders

### Activity
- `/activity` - See which teams are most active
- More activity = more upward price pressure

---

## 🏆 Achievements

Earn badges by hitting milestones! Use `/achievements` to track progress.

### Examples
- 🎯 **First Trade** - Make your first trade
- 💰 **Millionaire** - Reach 1M Spurs total value
- 💎 **Diamond Hands** - Hold a stock for 7+ days
- 🐋 **Whale** - Make a 100k+ Cog trade
- 🌈 **Diversified** - Own all 6 team stocks
- 👑 **Market Master** - Unlock all achievements

---

## 💡 Trading Tips

### For Beginners
1. **Start Small**: Don't invest everything in one stock
2. **Diversify**: Buy multiple teams to spread risk
3. **Watch Activity**: Active teams often have rising prices
4. **Use Alerts**: Set alerts to catch good entry points
5. **Check History**: Use `/history` to learn from past trades

### Strategy Ideas
- **Buy the Dip**: Set limit buys below current price
- **Take Profits**: Set limit sells above purchase price
- **Hold Long-term**: Diamond hands strategy for stable gains
- **Day Trading**: Quick buys/sells on price swings
- **Activity Trading**: Buy teams with increasing activity

### Common Mistakes
- ❌ Panic selling when prices drop
- ❌ Investing all money in one stock
- ❌ Ignoring team activity levels
- ❌ Not using limit orders
- ❌ Forgetting to check portfolio regularly

---

## 📉 Understanding Profit/Loss

### Your P/L
Profit/Loss shows if you're making or losing money:
- **Green +**: You're in profit
- **Red -**: You're at a loss
- **Percentage**: Return on investment (ROI)

### Example
You bought 10 STMP at 10 Cogs = 100 Cogs invested
- Now worth 150 Cogs = **+50 Cogs profit (+50%)**
- Now worth 80 Cogs = **-20 Cogs loss (-20%)**

### Realized vs Unrealized
- **Unrealized P/L**: Profit/loss if you sold now (shown in `/portfolio`)
- **Realized P/L**: Actual profit when you sell (shown in `/history`)

---

## 🎨 Reading Charts

### Line Charts (`/graph`)
- **X-axis**: Time
- **Y-axis**: Price in Cogs
- **Green line**: Bullish (ended higher)
- **Red line**: Bearish (ended lower)
- **High/Low markers**: Highest and lowest prices

### Candlestick Charts (`/candlestick`)
- **Green candle**: Price went up (Close > Open)
- **Red candle**: Price went down (Close < Open)
- **Wicks**: Show high/low range
- **Body**: Shows open/close range

**How to read a candle:**
1. Bottom of wick = Lowest price that hour
2. Top of wick = Highest price that hour
3. Body shows opening and closing prices
4. Bigger body = bigger price movement

---

## ⚠️ Rules & Limits

### Trading Rules
- Can't trade your own team's stock (prevents manipulation)
- Need enough cash for purchases
- Need to own shares to sell them
- Prices update every 3 minutes

### Feature Limits
- **Limit Orders**: Max 10 active at once, expire after 24h
- **Price Alerts**: Max 10 active at once, delete after triggering
- **Watchlist**: Max 10 stocks
- **Trade History**: Shows last 50 trades

### Cooldowns
- **Message Activity**: 60 second cooldown per user
- Prevents spam from affecting market unfairly

---

## 🤔 FAQ

**Q: Why can't I trade my own team?**
A: Anti-manipulation rule. You could spam messages to boost your own stock.

**Q: How often do prices update?**
A: Every 3 minutes based on activity, volatility, and momentum.

**Q: What happens to my limit orders if I log off?**
A: They stay active and auto-execute even when you're offline!

**Q: Do price alerts work multiple times?**
A: No, alerts delete after triggering once. Set a new one if needed.

**Q: Can I lose all my money?**
A: Stock prices can drop, but they won't go to zero. Trade carefully!

**Q: How do I become #1 on the leaderboard?**
A: Smart trading, diversification, and using advanced features like limit orders!

**Q: What's the difference between Cogs and Spurs?**
A: Just like dollars and cents. 1 Cog = 64 Spurs. Think Cogs = dollars.

---

## 🆘 Need Help?

- Use `/help` in Discord for command list
- Check your trade history with `/history` to analyze past moves
- Watch the leaderboard to see what top traders do
- Ask in the server - experienced traders love to share tips!

---

## 📚 Quick Command Reference

| Command | What It Does |
|---------|--------------|
| `/register` | Create account |
| `/balance` | Check cash |
| `/market` | View all stocks |
| `/buy STMP 10` | Buy 10 STMP shares |
| `/sell STMP 10` | Sell 10 STMP shares |
| `/portfolio` | View holdings |
| `/graph STMP` | Price chart |
| `/limitbuy STMP 5 12` | Auto-buy at 12 Cogs |
| `/alert STMP above 15` | Price alert |
| `/watch STMP` | Add to watchlist |
| `/history 7` | Trade history |
| `/achievements` | View badges |
| `/leaderboard` | Top traders |
| `/activity` | Team activity levels |

---

**Happy Trading! 📈💰**
