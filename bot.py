from telegram.ext import Updater, MessageHandler, Filters
from googletrans import Translator

TOKEN = "8742099805:AAFwuKPoXUpYWAc62mt2MkgIKv6OthOwwRQ"

translator = Translator()

def translate_text(update, context):
    text = update.message.text

    try:
        uz = translator.translate(text, dest='uz').text
        ru = translator.translate(text, dest='ru').text
        en = translator.translate(text, dest='en').text

        javob = f"""
🌐 Tarjimalar:

🇺🇿 O'zbek: {uz}
🇷🇺 Rus: {ru}
🇬🇧 English: {en}
"""
        update.message.reply_text(javob)

    except:
        update.message.reply_text("Xatolik yuz berdi 😔")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()