import discord
from discord.ext import commands
from apikeys import *

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)


@client.event
async def on_ready():
    print("Hello! I'm AiOBot. I'm now ready for use!")
    print("-----------------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am AiOBot. How can I help?")

@client.command()
async def goodbye(ctx):
    await ctx.send("Goodbye, sweet dreams!")

@client.command()
async def username(ctx):
    await ctx.send(client.user)

@client.event
async def on_member_join(member):
    channel = client.get_channel(JOIN_LEAVE_MESSAGE_CHANNEL)
    await channel.send("Welcome")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(JOIN_LEAVE_MESSAGE_CHANNEL)
    await channel.send("Goodbye!")


client.run(TOKEN)