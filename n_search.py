from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
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

#  поиск по Netflix

def netflix_search (film_name, *args, **kwargs):
    print('netflix_search')
    print(args)
    print(kwargs)
    try:
        driver.get('https://www.netflix.com/browse')
        driver.delete_all_cookies()
        print('netflix_started')

        #Подгрузка куки
        for cookie in pickle.load(open(f'netflix_cookies', 'rb')):
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(0.5)

        #Инициализация поиска
        search_start = driver.find_element(By.CLASS_NAME, 'searchBox')
        search_start.find_element(By.CLASS_NAME, 'searchTab').click()
        time.sleep(0.5)
        search_film_input = search_start.find_element(By.CLASS_NAME, 'searchInput')
        search_film = search_film_input.find_element(By.ID, 'searchInput')
        search_film.send_keys(film_name)
        time.sleep(1.5)

        #Получение ссылки
        get_first = driver.find_element(By.ID, 'appMountPoint')
        get_second = get_first.find_element(By.CLASS_NAME, 'mainView')
        get_three = get_second.find_element(By.CLASS_NAME, 'search')
        get_four = get_three.find_element(By.CLASS_NAME, 'galleryContent')
        get_eight = get_four.find_element(By.ID,'title-card-0-0')
        get_nine = get_eight.find_element(By.TAG_NAME, 'a')
        film_url = get_nine.get_attribute('href')
        
        return film_url
    
    except Exception as ex:
        logging.info(f'Flim {film_name} not found: {ex}')
        return 'Not_found'



