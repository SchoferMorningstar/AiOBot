import discord
from discord.ext import commands
from apikeys import *
import os
from tabs import *

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name = random_message(activities)))
    print("Hello! I'm AiOBot. I'm now ready for use!")
    print("-----------------------------------------")

initial_extensions = []

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        initial_extensions.append("cogs."+filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)


client.run(TOKEN)