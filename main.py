import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Hello! I'm AiOBot. I'm now ready for use!")
    print("-----------------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am AiOBot. How can I help?")

client.run('MTEyNDgwMjg0MzEzMjU3OTk1MA.GuYcfk.pj68jEomaKPN5NqkOKRYI3s4kE_nR-meMcC7BM')