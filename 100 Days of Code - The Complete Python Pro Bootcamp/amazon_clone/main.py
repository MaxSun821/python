import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()
TARGET_PRICE = 100
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# headers
header = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

price_text = soup.find(class_="a-offscreen").get_text()
price = float(price_text.split("$")[1])
print(price)
title = soup.find(id="productTitle").get_text().strip()
print(title)

if price < TARGET_PRICE:
    message = f"{title} is on sale for {price}!"
    with smtplib.SMTP(os.environ["smtp_server"]) as connection:
        connection.starttls()
        connection.login(user=os.environ["EMAIL"], password=os.environ["PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL"],
            to_addrs=os.environ["TO_EMAIL"],
            msg=f"Subject:Amazon Price Alert\n\n{message}\n{url}".encode("utf-8")
        )