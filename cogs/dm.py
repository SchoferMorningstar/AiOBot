import discord
from discord.ext import commands

class DM(commands.Cog):

    def __init__(self, client):
        self.client = client
    @commands.command()
    async def dm(self, ctx, member:discord.Member, *, message = "Witaj na serwerze"):
        await member.send(message)

async def setup(client):
    await client.add_cog(DM(client))