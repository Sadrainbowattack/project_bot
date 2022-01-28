from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
import time
from settings import n_login, n_password, driver_path


option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enables', False)
option.set_preference('dom.webnotifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')
url = 'https://www.netflix.com/ru/login'
driver = webdriver.Chrome(executable_path=driver_path)

try:
    driver.get(url=url)
    time.sleep(5)
    email_input = driver.find_element(By.ID, 'id_userLoginId')
    email_input.clear()
    email_input.send_keys(n_login)
    time.sleep(5)
    password_enter = driver.find_element(By.ID, 'id_password')
    password_enter.clear()
    password_enter.send_keys(n_password)
    time.sleep(5)
    password_enter.send_keys(Keys.ENTER)
    time.sleep(5)
    pickle.dump(driver.get_cookies(), open(f'netflix_cookies', 'wb'))
    time.sleep(3)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()