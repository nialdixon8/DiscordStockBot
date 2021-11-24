import discord
import requests

API_KEY = "KEY"#Use your own Alpha Vantage Key


#function to determine the stock price of a ticker
def stockPrice(stock):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={API_KEY}'
    r = requests.get(url)
    data = r.json()
    try:
        return data['Global Quote']['05. price']
    except KeyError:
        return "Invalid Stock Ticker"


client = discord.Client()

#run when bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#run when a message has been recieved
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #detect messages that start with a $ ticker symbol
    if message.content.startswith('$'):
        await message.channel.send(stockPrice(message.content[1:]))

client.run("TOKEN")#Use your own discord token