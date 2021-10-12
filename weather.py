import discord

#weather message
#to change border collor pick a hex value and set color = to 0x######
color = 0x0255E8
key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Daily Lows',
    'temp_max' : 'Daily High'
}

#this gets rid of humidity and pressure from the weather data given by
#OpenWeatherMap
def parse_data(data):
    data = data['main']
    del data['humidity']
    del data['pressure']
    return data

#building weather message
def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title = f'{location} Weather',
        description = f'Todays Weather:',
        color = color
    )
    for key in data:
        message.add_field(
            name = key_features[key],
            value = str(data[key]),
            inline = False
        )
    return message

#error message
def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description = f'There was an error retrieving weather for your {location}.',
        color = color
    )
