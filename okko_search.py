from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

# Настройка опций: обнаружение автоматизации, уведомления, звук, окно браузера
option = webdriver.FirefoxOptions() 
option.set_preference('dom.webdriver.enables', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
option.headless = True

driver = webdriver.Firefox(executable_path='C:\\projects\\project_bot\\geckodriver\\geckodriver', options=option)

#  поиск по okko.tv

def okkotv_search (film_name):
    print('okkotv_search')
    try:
        driver.get(f'https://okko.tv/search/{film_name}')
        print('okko_started')
        driver.delete_all_cookies()
        time.sleep(1)
        
        get_first = driver.find_element(By.CLASS_NAME, '_3se_G')
        get_second = get_first.find_element(By.CLASS_NAME, '_2_TsQ')
        get_three = get_second.find_element(By.TAG_NAME, 'a')
        film_url = get_three.get_attribute('href')

        return film_url     


    except Exception as ex:
        logging.info(f'Flim {film_name} not found: {ex}')
        return 'Not_found'
