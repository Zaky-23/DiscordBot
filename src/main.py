from discord import Intents
from bot import Bot

f = open('token.txt', 'r')
TOKEN = f.read()
f.close()

INTENTS = Intents.default()
INTENTS.message_content = True

client = Bot(intents=INTENTS)

client.run(TOKEN)