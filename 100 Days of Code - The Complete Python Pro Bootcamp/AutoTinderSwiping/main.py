from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")
sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="q2098069830"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="q369688754"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fb_login.click()

sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

fb_email = driver.find_element(By.NAME, value='email')
fb_password = driver.find_element(By.NAME, value='pass')
fb_email.send_keys("FBEMAIL")
fb_password.send_keys("FBPASSWORD")
fb_password.send_keys(Keys.ENTER)
sleep(25)
driver.switch_to.window(base_window)
print(driver.title)
