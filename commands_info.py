"""Info and statistics commands."""
import discord
from discord import app_commands
from discord.ext import commands
import market
import team_detection
import utils
import config


class InfoCommands(commands.Cog):
    """Information and statistics commands."""
    
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="activity", description="View team activity levels affecting market prices")
    async def activity(self, interaction: discord.Interaction):
        """Display team activity scores."""
        embed = discord.Embed(
            title="📊 Team Activity Levels",
            description="Message activity influences stock prices\nHigher activity = upward price pressure",
            color=0x57F287
        )
        
        # Get all activity scores
        activity_data = []
        for symbol in config.TEAMS.keys():
            score = market.market.get_activity_score(symbol)
            team_name = team_detection.get_team_name(symbol)
            activity_data.append((symbol, team_name, score))
        
        # Sort by activity
        activity_data.sort(key=lambda x: x[2], reverse=True)
        
        # Create activity bars
        max_score = max(score for _, _, score in activity_data) if activity_data else 1
        
        for symbol, team_name, score in activity_data:
            # Create visual bar
            bar_length = 20
            filled = int((score / max_score * bar_length)) if max_score > 0 else 0
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Activity level
            if score > 50:
                level = "🔥 Very High"
            elif score > 20:
                level = "📈 High"
            elif score > 5:
                level = "📊 Moderate"
            else:
                level = "📉 Low"
            
            embed.add_field(
                name=f"{symbol} - {team_name}",
                value=f"{bar}\n{level} • Score: {score:.1f}",
                inline=False
            )
        
        embed.add_field(
            name="ℹ️ How It Works",
            value=(
                "• Messages from team members increase activity\n"
                "• Activity affects price movement during updates\n"
                "• Scores decay over time\n"
                "• Updates every 3 minutes"
            ),
            inline=False
        )
        
        embed.set_footer(text="Send messages to boost your team's stock price!")
        
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="help", description="View bot commands and features")
    async def help_command(self, interaction: discord.Interaction):
        """Display help information."""
        embed = discord.Embed(
            title="📚 GSC - Gearfall Stock Exchange",
            description="Trade team stocks and build your fortune!\n━━━━━━━━━━━━━━━━━━━━",
            color=0x5865F2
        )
        
        # Trading Commands
        embed.add_field(
            name="💰 Basic Trading",
            value=(
                "`/register` - Create your trading account\n"
                "`/balance` - Check your wallet\n"
                "`/market` - View all stock prices\n"
                "`/stock <symbol>` - Stock details\n"
                "`/buy <symbol> <shares>` - Buy shares\n"
                "`/sell <symbol> <shares>` - Sell shares\n"
                "`/portfolio` - Your holdings with pie chart"
            ),
            inline=False
        )
        
        # Analysis Commands
        embed.add_field(
            name="📊 Analysis & Charts",
            value=(
                "`/graph <symbol>` - Live updating price chart\n"
                "`/candlestick <symbol>` - OHLC candlestick chart\n"
                "`/history [days] [symbol]` - Your trade history\n"
                "`/activity` - Team activity levels\n"
                "`/leaderboard` - Top traders"
            ),
            inline=False
        )
        
        # Advanced Trading
        embed.add_field(
            name="🎯 Advanced Trading",
            value=(
                "`/limitbuy <symbol> <shares> <price>` - Auto-buy at target\n"
                "`/limitsell <symbol> <shares> <price>` - Auto-sell at target\n"
                "`/orders` - View your limit orders\n"
                "`/cancelorder <id>` - Cancel an order"
            ),
            inline=False
        )
        
        # Alerts & Watchlist
        embed.add_field(
            name="🔔 Alerts & Watchlist",
            value=(
                "`/alert <symbol> <above/below> <price>` - Price alert\n"
                "`/alerts` - View your alerts\n"
                "`/watch <symbol>` - Add to watchlist\n"
                "`/watchlist` - View watchlist with 24h changes"
            ),
            inline=False
        )
        
        # Achievements
        embed.add_field(
            name="🏆 Achievements",
            value="`/achievements` - View unlocked badges and progress",
            inline=False
        )
        
        # Market Info
        embed.add_field(
            name="📈 Market Info",
            value=(
                "• Prices update every **3 minutes**\n"
                "• Activity + volatility + momentum\n"
                "• Starting balance: **10 Cogs**\n"
                "• 1 Cog = 64 Spurs\n"
                "• Limit orders auto-execute\n"
                "• Alerts send you DMs"
            ),
            inline=False
        )
        
        # Available Stocks
        stocks = ", ".join([f"{s}" for s in config.TEAMS.keys()])
        embed.add_field(
            name="🏢 Available Stocks",
            value=stocks,
            inline=False
        )
        
        # Admin commands (only show to admins)
        if isinstance(interaction.user, discord.Member):
            admin_role = discord.utils.get(interaction.user.roles, id=config.ADMIN_ROLE_ID)
            if admin_role:
                embed.add_field(
                    name="🛡️ Admin Commands",
                    value=(
                        "`/give <user> <cogs>` - Give Cogs to player\n"
                        "`/take <user> <cogs>` - Take Cogs from player\n"
                        "`/setprice <symbol> <price>` - Set stock price\n"
                        "`/resetmarket` - Reset all prices\n"
                        "`/ratebuild <symbol> <rating>` - Rate team build (1-10)\n"
                        "`/heat <symbol>` - Apply HEAT buff (+25%)"
                    ),
                    inline=False
                )
        
        embed.set_footer(text="Full docs: github.com/InfernoHost/vn-stocks • Use /stock for quick trading!")
        
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot):
    """Setup function for loading the cog."""
    await bot.add_cog(InfoCommands(bot))
