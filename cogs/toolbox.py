import discord
from discord.ext import commands
from cogs.toolbox_lib import NOMICS_EXCH_RT_URL, fetch_exchange

class Toolbox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def c_to_f(self, ctx, temp):
        """

        Converts input to fahrenheit.

        """
        c_temp = int(temp)
        f_temp = (c_temp * 9 / 5) + 32

        await ctx.send(f"{ctx.author.name}: {f_temp}")

    @commands.command()
    async def crypt_coin(self, ctx):
        await ctx.send(f"{fetch_exchange()}")



def setup(bot):
	bot.add_cog(Toolbox(bot))