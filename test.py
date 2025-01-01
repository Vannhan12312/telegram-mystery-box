from telegram import Bot

TELEGRAM_TOKEN = "7590599617:AAEFuu9lFiDd9EgRSN52APrN8LtQIxrDWRw"
bot = Bot(token=TELEGRAM_TOKEN)

# In thông tin bot
print(bot.get_me())
