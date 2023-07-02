@client.command()
async def dm(ctx, member:discord.Member, *, message = "Witaj na serwerze"):
    await member.send(message)