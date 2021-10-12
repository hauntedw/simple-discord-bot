import discord
import random
import requests
import json
from discord.ext import commands, tasks
from pprint import pprint
from weather import *
from itertools import cycle

#using ? as command identifier
client = commands.Bot(command_prefix = '?')
#list of bot status messages
status = cycle(['With Your Heart', 'Claw Machine Simulator', 'The NASA Space Physical'])

#notifies that the bot is ready for use
@client.event
async def on_ready():
    change_status.start()
    print("Bot is ready.")

#when someone sends a unused commands it will send an error and prompt them to see command list
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used. Please use ?help for list of commands.')

#changes bot status message on discord every minute
@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#sends user ping to servers
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

#8ball responses
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Don’t count on it.',
                 'It is certain.',
                 'It is decidedly so.',
                 'Most likely.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Outlook good.',
                 'Reply hazy, try again.',
                 'Signs point to yes.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Yes.',
                 'Yes – definitely.',
                 'You may rely on it.']
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

#weather using OpenWeatherMap api in Celsius
@client.command()
async def weatherC(ctx, *, location):
    if len(location) >= 1:
        location.lower()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
        data = json.loads(requests.get(url).content)
        data = parse_data(data)
    try:
        await ctx.send(embed=weather_message(data, location))
    except KeyError:
        await ctx.send(f"Error: Invalid Location")

#weather using OpenWeatherMap api in Farenheit
@client.command()
async def weatherF(ctx, *, location):
    if len(location) >= 1:
        location.lower()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
        data = json.loads(requests.get(url).content)
        data = parse_data(data)
    try:
        await ctx.send(embed=weather_message(data, location))
    except KeyError:
        await ctx.send(f"Error: Invalid Location")

#shutsdown bot
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

api_key = 'your api key'
client.run('your discord bot key')
