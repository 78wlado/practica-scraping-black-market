import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from telegram_bot import TelegramBot
#from mongodb import MongoDB

chrome_driver = webdriver.Chrome()
bot = TelegramBot()
#db = MongoDB()

chrome_driver.get("https://www.backmarket.com/en-us")
print(chrome_driver.title)

search_box = chrome_driver.find_element(By.ID, "desktop-searchbar")
search_box.send_keys("iphone")
search_button = chrome_driver.find_element(By.CSS_SELECTOR, "#__layout > div > div > div.sticky.top-0.z-20.h-\[10\.4rem\].md\:h-\[10rem\].transition-all.duration-200.ease-in-out > header > div.relative.flex.items-center.justify-between.w-full.px-6.py-4.md\:px-7.md\:py-5 > div.flex.items-center.justify-end.md\:h-\[3\.2rem\].w-full > div.hidden.md\:mr-4.lg\:mr-6.md\:w-full.md\:block > form > div.flex.items-center.bg-white.text-black.pl-6.rounded-2.overflow-hidden > button:nth-child(3) > svg")
search_button.click()

content = chrome_driver.find_element(By.CLASS_NAME, "grid")
print(content.text)
text = content.text
bot.send_tg_message(text)


time.sleep(2)
chrome_driver.get("https://www.backmarket.com/en-us")

print("fin")
chrome_driver.close()