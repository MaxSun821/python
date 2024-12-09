from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price_whole.text}.{price_fraction.text}")

# price_whole = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
# print(price_whole.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)
driver.quit()