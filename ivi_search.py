from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
from settings import driver_path


# Настройка опций: обнаружение автоматизации, уведомления, звук, окно браузера
option = webdriver.FirefoxOptions() 
option.set_preference('dom.webdriver.enables', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.headless = True

driver = webdriver.Firefox(executable_path=driver_path, options=option)

#  поиск по ivi.ru

def iviru_search (film_name):
    print('iviru_search')
    try:
        driver.get('https://www.ivi.ru/search/')
        print('ivi_started')
        driver.delete_all_cookies()
        time.sleep(1)

        # Инициализация поиска
        start_search = driver.find_element(By.CLASS_NAME, 'search')
        second_search = start_search.find_element(By.CLASS_NAME, 'nbl-input__body')
        three_search = second_search.find_element(By.CLASS_NAME, 'nbl-input__editbox')
        three_search.send_keys(film_name)
        three_search.send_keys(Keys.ENTER)
        time.sleep(2)

        # Получение ссылки на фильм
        get_first = driver.find_element(By.CLASS_NAME, 'searchBlock__container')
        get_second = get_first.find_element(By.CLASS_NAME, 'searchBlock__contentVirtual')
        get_three = get_second.find_element(By.TAG_NAME, 'a')
        film_url = get_three.get_attribute('href')
        
        return film_url

    except Exception as ex:
        logging.info(f'Flim {film_name} not found: {ex}')
        return 'Not_found'
