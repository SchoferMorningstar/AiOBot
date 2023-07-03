import discord
from discord.ext import commands
from tabs import *
from apikeys import *
from functions import *

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Użytkownik {member.name} otrzymał kikca z powody {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Nie masz uprawnień do dawania kicków na tym serwerze")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Użytkownik {member.name} został zbanowany z powodu {reason}')

    @kick.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Nie masz uprawnień do banowania na tym serwerze")

async def setup(client):
    await client.add_cog(Moderator(client))