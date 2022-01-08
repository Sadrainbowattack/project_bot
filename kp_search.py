from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time

url = 'https://www.kinopoisk.ru/'
driver = webdriver.Chrome(executable_path='C:\\projects\\project_bot\\chromedriver\\chromedriver')

def kinp_search(film_name):
    try:
        driver.get(url=url)
        time.sleep(1)
        driver.delete_all_cookies()

#        for cookie in pickle.load(open(f'kp_cookies', 'rb')):
#           driver.add_cookie(cookie)
#        time.sleep(2)
#        driver.refresh()
#        time.sleep(1)

        find_film = driver.find_element(By.NAME, 'kp_query')
        find_film.send_keys(film_name)
        time.sleep(1)
        find_film.send_keys(Keys.ENTER)
        time.sleep(2)

        get_first = driver.find_element(By.ID, 'content_block')
        get_second = get_first.find_element(By.CLASS_NAME, 'search_results')
        get_three = get_second.find_element(By.CLASS_NAME, 'info')
        get_four = get_three.find_element(By.TAG_NAME, 'a')
        film_url = get_four.get_attribute('href')
        return film_url

    except Exception as ex:
        print(ex)
        return 'Not_found'

