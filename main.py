import discord
from discord.ext import commands
from apikeys import *
import datetime as dt
import requests
import json

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

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
    await ctx.send(f"Weather in {city} \nTemperature: {temp:.2f}°C \nFeels like temperature: {feels_temp:.2f}°C \nHumidity: {humidity}% \nWind speed: {wind_speed}m/s \nGeneral description: {desc} \nSunrise time: {sunrise_time} local time \nSunset time: {sunset_time} local_time")



client.run(TOKEN)