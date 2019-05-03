from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token='832662397:AAFfKUi8HQqzhOJVgKOEp2L8InKl6cWaFpI')
dispatcher = updater.dispatcher
updater.start_polling()

def handler(bot, update):
    text = update.message.text
    chat_id = update.message.chat_id

    if 'die' in text:
        bot.send_message(chat_id=chat_id, text='suicide is a permanent solution to a temporary problem.')
    elif 'give up' in text:
        bot.send_message(chat_id=chat_id, text='Never give up on what you really want to do. The person with big dreams is more powerful than the one with all the facts.')
    elif 'cry' in text:
        bot.send_message(chat_id=chat_id, text='Let your tears come. Let them water your soul.')
    elif 'run' in text:
        bot.send_message(chat_id=chat_id, text='Running away from things you find unpleasant causes suffering. But facing and challenging such situations will enrich your life.')
    elif 'regret' in text:
        bot.send_message(chat_id=chat_id, text='Regrets only apply when we don\'t learn from a situation. No sense looking back, look forward with new knowledge and no regret.') 
    elif 'jealous' in text:
        bot.send_message(chat_id=chat_id, text='Jealousy is the father of success.')

    elif 'thank' in text:
        bot.send_message(chat_id=chat_id, text='you are welcome:)')

    elif 'sad' in text:
        bot.send_message(chat_id=chat_id, text='Sometimes pain is so unmanageable that the idea of spending another day with it seems impossible. Other times pain acts as a compass to help you through the messier tunnels of growing up. But pain can only help you find happiness if you remember it.')

    elif 'mad' in text:
        bot.send_message(chat_id=chat_id, text='If you are patient in one moment of anger, you will escape a hundred days of sorrow.')

    elif 'anxious' in text:
        bot.send_message(chat_id=chat_id, text='Anxiety is the dizziness of freedom.')

    elif 'upset' in text:
        bot.send_message(chat_id=chat_id, text='Life happens. There is no point in being upset or down about things we can\'t control or change.')

    elif 'hi' in text:
        bot.send_message(chat_id=chat_id, text='hi')
        bot.send_message(chat_id=chat_id, text='how do you feel today?')

    elif 'bye' in text:
        bot.send_message(chat_id=chat_id, text='bye bye, have a nice day')

    else:
        bot.send_message(chat_id=chat_id, text='are you okay? I want to help you.')

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
