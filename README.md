# simple-discord-bot
discord bot made with python and discord.py\
bot.py is your bot commands\
weather.py pulls weather data from OpenWeatherMap and builds a weather message

Set-up:\
You will want to get Requests for Python found here: https://docs.python-requests.org/en/latest/ 
this lets us process http in order to call for weather data.\
You will also need the Python Discord Library: https://discordpy.readthedocs.io/en/stable/
the quickstart guide on both sites will get you started on downloading and setting them up for importing into the bot and weather file.\
Next you will need to get your api key for OpenWeatherMap here: https://openweathermap.org/price the free service should be fine for most servers. As a side note it did take me around 10 minutes for my key to be activated once I got it sent to my email.\
Finally you will need to create your discord bot account. Simply go here: https://discord.com/developers/applications and create a new application.\
Once you have made a new application you will need its Public Key it should be found under the ID.
![bot-id](https://i.imgur.com/MJ9VEkX.png)\
Once you have all those just plug in the Public Key and API Key and your program should be good to go. As a note I ran my code on Atom.\
\
TO-DO:\
Polling System to allow server users to vote on different topics.\
Suggestion box system for different servers to put input what they want to see from the bot.\
Auto-mod that checks users messages against blacklist of words not allowed on server.\
Alarm / Notification fuction that notifies users in dms or by @ing in server to remind them of something.\
Random fact of the day.
