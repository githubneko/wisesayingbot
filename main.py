import telegram

api_key = '832662397:AAFfKUi8HQqzhOJVgKOEp2L8InKl6cWaFpI'

bot = telegram.Bot(token=api_key)

# chat_id = bot.get_updates() [-1].message.chat_id

chat_id = 891303764

bot.sendMessage(chat_id=chat_id, text='hello')
