import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Bot Is Online!')
    print(bot.user.name)
    print(bot.user.id)
    print('|||||||')

@bot.command()
async def ping():
    await bot.say(':ping_pong:')
@bot.command()
async def render(type):
    await bot.say('https://growtopiagame.com/worlds/%27f%27%7Btype%7D.png%27)
@bot.command()
async def hack():
     await bot.say('coming soon!')
@bot.command(pass_context = True)
async def say(ctx, *, msg: str):
      await bot.say(msg)
      await bot.delete_message(ctx.message)

bot.run('NTI2NjA0OTA0MTI3NzkxMTI0.DyViqg.sKPaLtP1k-67kfu6oKyZm2Uxk8w')
