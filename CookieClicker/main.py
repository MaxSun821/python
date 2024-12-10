import time

from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

cookie = driver.find_element(By.ID, value="cookie")
timeout = time.time() +  5
five_min = time.time() + 5 * 60

while True:
    cookie.click()
    if time.time() > timeout:
        cookie_num = driver.find_element(By.ID, value="money").text
        all_price = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_price = []

        for price in all_price:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_price.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]] = item_ids[n]
        if "," in cookie_num:
            cookie_num = cookie_num.replace(",", "")
        money = int(cookie_num)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id
        highest_price_affordable_upgrades = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrades]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break
driver.quit()