import os
from keep_alive import keep_alive
from discord.ext import commands

botFunctions = ['!help', '!subs']

client = commands.Bot(command_prefix='')
client.remove_command('help')


@client.event
async def on_ready():
    print('logged in')


@client.command()
async def hello(ctx):
    await ctx.send('Goodbye')

@client.command()
async def goodbye(ctx):
  await ctx.send("hello")

@client.command()
async def why(ctx):
  await ctx.send("power")

@client.command()
async def help(ctx):
    await ctx.send(
        "Hello! I'm a bot!\nHere is a list of functions you can try:")

    str = ''
    for item in botFunctions:
        str += (item + '\n')
    await ctx.send(str)


@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return

    if message.author.bot:  # checks if author is a bot
        return

    await client.process_commands(message)


my_secret = os.environ['TOKEN']

keep_alive()
client.run(os.getenv('TOKEN'))
