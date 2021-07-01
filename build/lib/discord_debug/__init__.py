from discord.ext import commands
import discord
import os
import sys

class discord_debug(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      
    @commands.group(aliases="dd")
    async def discord_debug(self,ctx):
      if ctx.invoked_subcommand is None:
        await ctx.send('A subcommand is required after the main command.')
    
    @dd.command()
    @commands.is_owner()
    async def restart(self,ctx):
      await ctx.send("restarting")
      await self.bot.change_presence(status=discord.Status.idle,activity=discord.Game(name='restarting🔄', type=1))
      python = sys.executable
      os.execl(python, python, *sys.argv)
      
    @dd.command()
    @commands.is_owner()
    async def reload(self,ctx,text):
      self.bot.reload_extension(text)
      
    @dd.command()
    @commands.is_owner()
    async def load(self,ctx,text):
      self.bot.load_extension(text)
      
    @dd.command()
    @commands.is_owner()
    async def unload(self,ctx,text):
      self.bot.unload_extension(text)
      
def setup(bot):
  return bot.add_cog(discord_debug(bot))