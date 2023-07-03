import discord
from discord.ext import commands
from tabs import *
from apikeys import *
from functions import *

class Grettings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(JOIN_LEAVE_MESSAGE_CHANNEL)
        await member.send(f"Witaj na serwerze {member.mention}")
        await channel.send(ON_MEMBER_JOIN_MESSAGE)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.client.get_channel(JOIN_LEAVE_MESSAGE_CHANNEL)
        await channel.send(ON_MEMBER_LEAVE_MESSAGE)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(random_message(hello_messages))

    @commands.command()
    async def goodbye(self, ctx):
        await ctx.send(random_message(goodbye_message))

async def setup(client):
    await client.add_cog(Grettings(client))

