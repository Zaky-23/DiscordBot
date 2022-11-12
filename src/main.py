from discord import Intents
from bot import Bot

TOKEN = "MTA0MTAwNjMzOTU0MDkxNDIwNg.GAfpGC.Lsd_w_b03Hig3bsrpJkXQ3I8ydu6mDXoM1ABN0"

INTENTS = Intents.default()
INTENTS.message_content = True

client = Bot(intents=INTENTS)

client.run(TOKEN)