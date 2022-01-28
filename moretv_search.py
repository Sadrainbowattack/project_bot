# from selenium import webdriver
# from selenium.webdriver.common import keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import pickle
# import time

# url = 'https://more.tv/'
# driver = webdriver.Chrome(executable_path='C:\\projects\\project_bot\\chromedriver\\chromedriver')

# # поиск по More.tv 

# def more_search(film_name):
#     print('more_search')
#     try:
#         driver.get(url=url)
#         driver.delete_all_cookies()
#         time.sleep(1)

#         #Инициализация поиска
#         search_start = driver.find_element(By.CLASS_NAME, 'Desktop')
#         find_search_tab = search_start.find_element(By.CLASS_NAME, 'Container-module__container-default--BPN8K')
#         find_search_tab.find_element(By.CLASS_NAME, 'HeaderView-module__search--OlKXZ').click()
#         time.sleep(1)
#         first_search_enter = driver.find_element(By.ID, 'modals')
#         second_search_enter = first_search_enter.find_element(By.CLASS_NAME, 'BlackOut-module__blackout--JuXwM BlackOut-module__top--Uz8Wj')
#         search_film = second_search_enter.find_element(By.CLASS_NAME, 'SearchBar-module__field--htVpM')
#         search_film.send_keys(film_name)
#         time.sleep(2)
        
#         #Получение ссылки
#         get_first = driver.find_element(By.ID, 'modals')
#         get_second = get_first.find_element(By.ID, 'blackout-container')
#         get_three = get_second.find_element(By.CLASS_NAME, 'SearchResult-module__result--owkOr')
#         get_four = get_three.find_element(By.CLASS_NAME, 'index-module__sliderWrapper--qdZaI')
#         get_five = get_four.find_element(By.TAG_NAME, 'a')
#         film_url = get_five.get_attribute('href')
        
#         return film_url

#     except Exception as ex:
#         print(ex)
#         return 'Not_found'

# if __name__ == "__main__":
#     more_search('Никто')

    
    