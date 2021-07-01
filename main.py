from discord.ext import commands
import os

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print(f'{bot.user.name}でログインしました')

@bot.command
async def ping(ctx):
  await ctx.send("a")
  
bot.run(os.getenv("TOKEN"))