from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(30)
driver.find_element(By.ID, "langSelect-EN").click()
driver.implicitly_wait(30)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
# actions.click(cookie) # pressing the cookie
#
# for i in range(5000):
#     actions.click(cookie)
#     if i % 50 == 0:
#         actions.perform()
#         actions.reset_actions()
#     count = int(cookie_count.text.split(" ")[0])
#     for item in items:
#         value = int(item.text)
#         if value <= count:
#             upgrade_actions = ActionChains(driver)
#             upgrade_actions.move_to_element(item)
#             upgrade_actions.click()
#             upgrade_actions.perform()

upgrade_actions = ActionChains(driver)

for i in range(5000):
    actions.click(cookie)
    if i % 50 == 0:
        actions.perform()
        actions.reset_actions()

    count = int(cookie_count.text.split(" ")[0])
    if count >= 100:  # Example: Upgrade when you have 1 million cookies
        # Find the most expensive upgrade and buy it
        max_price = -1
        max_price_item = None
        for item in items:
            value = int(item.text)
            if value > max_price and value <= count:
                max_price = value
                max_price_item = item
        if max_price_item:
            upgrade_actions.move_to_element(max_price_item)
            upgrade_actions.click()
            upgrade_actions.perform()

    upgrade_actions.reset_actions()

