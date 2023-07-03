import discord
from discord.ext import commands
from functions import *
import asyncio

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.turn = None
        self.turn_sign = "O"
        self.players = []
        self.game_channel = None

    @commands.command()
    async def ttt(self, ctx, member: discord.Member):
        self.turn = ctx.author
        self.players = [ctx.author, member]
        self.game_channel = ctx.channel

        message = await ctx.send(board_generate(self.tablica))

        def check(msg):
            return (
                msg.author == self.turn
                and msg.channel == self.game_channel
                and msg.content.isdigit()
                and 1 <= int(msg.content) <= 9
            )

        while True:
            try:
                msg = await self.client.wait_for('message', timeout=300.0, check=check)
            except asyncio.TimeoutError:
                self.turn = switch_turn(self.turn, self.players)
                self.turn_sign = switch_turn_sign(self.turn_sign)
                await ctx.send(f"Czas na ruch minął. Gracz {self.turn} grający {self.turn_sign} wygrywa walkowerem")
                break

            if msg.content.lower() == 'q':
                await ctx.send(f"Użytkownik {msg.author} przerwał grę.")
                break

            elif 1 <= int(msg.content) <= 9:
                if 1 <= self.tablica[int(msg.content) - 1] <= 9:
                    self.tablica[int(msg.content) - 1] = self.turn_sign
                    await message.edit(content=board_generate(self.tablica))
                    win = check_win(self.tablica)
                    if win is False:
                        self.turn = switch_turn(self.turn, self.players)
                        self.turn_sign = switch_turn_sign(self.turn_sign)
                        await msg.delete()
                    else:
                        await ctx.send(f"Wygrał {self.turn} grający {self.turn_sign}")
                        msg.delete()
                        break
                else:
                    await ctx.send("To pole jest zajęte")
            else:
                await ctx.send("Nieprawidłowe pole")

async def setup(client):
    await client.add_cog(Fun(client))
