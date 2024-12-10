import time

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
to_buy = [123456789, 1000000, 50000, 7000, 2000, 500, 100]
begin = time.time()
while True:
    cookie.click()
    end = time.time()
    if end - begin >= 5:
        cookie_num = driver.find_element(By.ID, value="money")
        # print(int(cookie_num.text))
        # break
driver.quit()