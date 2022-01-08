import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import time
from kp_search import kinp_search
from n_search import netflix_search
from moretv_search import more_search

logging.basicConfig(filename="bot.log", level=logging.INFO)


def greet_user(update, context):
    update.message.reply_text("Здравствуй, пользователь! Для поиска фильма введи - /search 'Название фильма'")

def search_film(update, context):
    update.message.reply_text('Минуточку, начал поиск')
    film_name = " ".join(map(str, context.args))
    kp_search_result = kinp_search(film_name)
    n_search_result = netflix_search(film_name)
    m_search = more_search(film_name)

    update.message.reply_text(f'Самые похожие результаты')
    time.sleep(1)
    update.message.reply_text(f'Кинопоиск - {kp_search_result}')
    update.message.reply_text(f'Netflix - {n_search_result}')
    update.message.reply_text(f'More.tv - {m_search}')
    

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("search", search_film))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()