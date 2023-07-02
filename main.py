import discord
from discord.ext import commands
from apikeys import *
import datetime as dt
import requests
import json
from discord.ext.commands import has_permissions, MissingPermissions
import os
import random
from tabs import *

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def random_message(tab):
    a = 0
    b = len(tab) - 1
    rand = random.randint(a,b)
    return tab[rand]


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.playing, name = random_message(activities)))
    print("Hello! I'm AiOBot. I'm now ready for use!")
    print("-----------------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send(random_message(hello_messages))

@client.command()
async def goodbye(ctx):
    await ctx.send(random_message(goodbye_message))

@client.command()
async def username(ctx):
    await ctx.send(client.user)

@client.event
async def on_member_join(member):
    channel = client.get_channel(JOIN_LEAVE_MESSAGE_CHANNEL)
    await channel.send(ON_MEMBER_JOIN_MESSAGE)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(JOIN_LEAVE_MESSAGE_CHANNEL)
    await channel.send(ON_MEMBER_LEAVE_MESSAGE)

@client.command()
async def weather(ctx, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_TOKEN}'
    response = requests.get(url)
    data = response.json()
    temp = kelvin_to_celsius(data['main']['temp'])
    feels_temp = kelvin_to_celsius(data['main']['feels_like'])
    humidity = data['main']['humidity']
    desc = data['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    wind_speed = data['wind']['speed']
    embed = discord.Embed(title = f'Pogoda w {city}', description = '', color=0x00ffff)
    embed.set_author(name="OpenWeather", url='https://openweathermap.org', icon_url = 'https://imgur.com/RvbHVqQ.png')
    embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/The_Weather_Channel_logo_2005-present.svg/225px-The_Weather_Channel_logo_2005-present.svg.png')
    embed.add_field(name="Ogólna pogoda ", value=f'{desc}', inline=False)
    embed.add_field(name="Temperatura: ", value=f'{temp:.2f}°C', inline=False)
    embed.add_field(name="Temperatura odczuwalna: ", value=f'{feels_temp:.2f}°C', inline=False)
    embed.add_field(name="Wilgotność: ", value=f'{humidity}%', inline=False)
    embed.add_field(name="Prędkość wiatru: ", value=f'{wind_speed}m/s', inline=False)
    embed.add_field(name="Wschód słońca: ", value=f'{sunrise_time} czasu lokalnego', inline=False)
    embed.add_field(name="Zachód słońca: ", value=f'{sunset_time} czasu lokalnego', inline=False)
    embed.set_footer(text="Informacje pogodowe dostarcza OpenWeather")
    await ctx.send(embed = embed)

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

client.run(TOKEN)