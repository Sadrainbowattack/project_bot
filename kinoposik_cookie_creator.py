from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time
from settings import kp_login, kp_password

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomatiomControlled')
url = 'https://passport.yandex.ru/auth?origin=kinopoisk&retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fpush%3Fretpath%3Dhttps%253A%252F%252Fwww.kinopoisk.ru%252Fapi%252Fprofile-pending%252F%253Fretpath%253Dhttps%25253A%25252F%25252Fwww.kinopoisk.ru%25252F%26uuid%3Dceac0cce-1cda-4076-b350-dc619b8e8809'
driver = webdriver.Chrome(executable_path='C:\\projects\\project_bot\\chromedriver\\chromedriver')

try:
    driver.get(url=url)
    time.sleep(2)
    email_input = driver.find_element(By.ID, 'passp-field-login')
    email_input.clear()
    email_input.send_keys(kp_login)
    time.sleep(2)
    email_confirm = driver.find_element(By.ID, 'passp:sign-in').click()
    time.sleep(3)
    password_enter = driver.find_element(By.ID, 'passp-field-passwd')
    password_enter.clear()
    password_enter.send_keys(kp_password)
    time.sleep(3)
    password_confirm = driver.find_element(By.ID, 'passp:sign-in').click()
    time.sleep(3)
    first_enter = driver.find_element(By.CLASS_NAME, 'passp-button').click()
    time.sleep(30) 
    second_enter = driver.find_element(By.CLASS_NAME, 'passp-button').click()
    time.sleep(3)
    pickle.dump(driver.get_cookies(), open(f'kp_cookies', 'wb'))
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()