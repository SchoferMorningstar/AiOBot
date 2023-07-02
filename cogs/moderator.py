@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Użytkownik {member} otrzymał kikca z powody {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do dawania kicków na tym serwerze")

@client.command()
@has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Użytkownik {member} został zbanowany z powodu {reason}')

@kick.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Nie masz uprawnień do banowania na tym serwerze")