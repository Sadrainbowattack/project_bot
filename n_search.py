from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time

url = 'https://www.netflix.com/browse'
driver = webdriver.Chrome(executable_path='C:\\projects\\project_bot\\chromedriver\\chromedriver')

def netflix_search (film_name):
    try:
        driver.get(url=url)
        driver.delete_all_cookies()

        for cookie in pickle.load(open(f'netflix_cookies', 'rb')):
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.refresh()
        time.sleep(1)

        search_start = driver.find_element(By.CLASS_NAME, 'searchBox')
        search_start.find_element(By.CLASS_NAME, 'searchTab').click()
        time.sleep(1)
        search_film_input = search_start.find_element(By.CLASS_NAME, 'searchInput')
        time.sleep(1)
        search_film = search_film_input.find_element(By.ID, 'searchInput')
        search_film.send_keys(film_name)
        time.sleep(3)
        get_first = driver.find_element(By.ID, 'appMountPoint')
        get_second = get_first.find_element(By.CLASS_NAME, 'mainView')
        get_three = get_second.find_element(By.CLASS_NAME, 'search')
        get_four = get_three.find_element(By.CLASS_NAME, 'galleryContent')
        get_eight = get_four.find_element(By.ID,'title-card-0-0')
        get_nine = get_eight.find_element(By.TAG_NAME, 'a')
        film_url = get_nine.get_attribute('href')
        
        return film_url
    
    except Exception as ex:
        print(ex)
        return 'Not_found'



