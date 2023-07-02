@client.command()
async def weather(ctx, city = "Warszawa"):
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