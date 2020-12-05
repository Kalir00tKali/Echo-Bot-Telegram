

#Production by Berlin
#Telegram - @por0vos1k



import logging  
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CommandHandler

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='botik.log'
                    )


def start_bot(update: Update, context: CallbackContext):
    mytext = "Hello! I am an echo bot".format
    (update.message.chat.first_name, '/start')
    logging.info
    ("User {} tap /start".format(update.message.chat.username))
    update.message.reply_text(mytext)


def chat(update: Update, context: CallbackContext):
    text = update.message.text
    logging.info(text)
    update.message.reply_text(text)


def main():
    print("Start")

    updater = Updater(
        token="text",
        use_context=True,
        )

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    logging.info("Bot started")
    main()
