import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import threading
import concurrent.futures
from kp_search import kinp_search
from n_search import netflix_search
from okko_search import okkotv_search
from ivi_search import iviru_search
from db_query import find_film_urls, save_film, save_urls, save_user_request


logging.basicConfig(filename="bot.log", level=logging.INFO)

# Приветствие Юзера
def greet_user(update):
    update.message.reply_text("Здравствуй, пользователь! Для поиска фильма введи - /search 'Название фильма'")


# Поиск фильма
def search_film(update, context):
    update.message.reply_text('Начал поиск. Обычно это занимет не больше минуты')
    film_name = " ".join(map(str, context.args))
    if film_name == '' or None:
        update.message.reply_text('Введите название фильма')
    else:
        kp_search_result = kinp_search(film_name)

        film_urls_pool = []

        # Запуск тредов
        with concurrent.futures.ThreadPoolExecutor() as exexutor:
            n_search_result = exexutor.submit(netflix_search, film_name,)
            okko_search_result = exexutor.submit(okkotv_search, film_name,)
            ivi_search_result = exexutor.submit(iviru_search, film_name,)

            film_urls_pool.append(n_search_result.result())
            film_urls_pool.append(okko_search_result.result())
            film_urls_pool.append(ivi_search_result.result())

        # Ответ пользователю
        update.message.reply_text(f'Самые похожие результаты')
        update.message.reply_text(f'Кинопоиск - {kp_search_result[1]}')
        update.message.reply_text(f'Netflix - {film_urls_pool[0]}')
        update.message.reply_text(f'Okko.tv - {film_urls_pool[1]}')
        update.message.reply_text(f'Ivi.ru - {film_urls_pool[2]}')
        
        # Сохранение в Бд
        save_film(kp_search_result[0])
        save_user_request(kp_search_result[0], film_name)
        save_urls(kp_search_result[0], kp_search_result[1], film_urls_pool[0], film_urls_pool[1], film_urls_pool[2])
            


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