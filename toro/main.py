import toro
from config import api_key_discord

bot = toro.ToroBot(city='Porto Alegre', state='RS', country='BR')
bot.run(api_key_discord)