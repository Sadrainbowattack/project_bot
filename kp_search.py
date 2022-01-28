from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

# Настройка опций: обнаружение автоматизации, уведомления, звук, окно браузера
option = webdriver.FirefoxOptions() #Настройка опций: обнаружение автоматизации, уведомления, звук, окно браузера
option.set_preference('dom.webdriver.enables', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
# option.headless = True

driver = webdriver.Firefox(executable_path='C:\\projects\\project_bot\\geckodriver\\geckodriver', options=option)

# поиск по Кинопоиску 

def kinp_search(film_name):
    try:
        driver.get('https://www.kinopoisk.ru/')
        time.sleep(0.5)
        print('kp_started')
        driver.delete_all_cookies()

        # Инициализация поиска
        find_film = driver.find_element(By.NAME, 'kp_query')
        find_film.send_keys(film_name)
        time.sleep(1)
        find_film.send_keys(Keys.ENTER)
        time.sleep(1)

        # Получение ссылки на фильм
        get_first = driver.find_element(By.ID, 'content_block')
        get_second = get_first.find_element(By.CLASS_NAME, 'search_results')
        get_three = get_second.find_element(By.CLASS_NAME, 'info')
        get_four = get_three.find_element(By.TAG_NAME, 'a')
        film_real_name = get_four.text
        film_url = get_four.get_attribute('href')

        return film_real_name, film_url

    except Exception as ex:
        logging.info(f'Flim {film_real_name} not found: {ex}')
        return 'Not_found'

if __name__ == "__main__":
    kinp_search('')
