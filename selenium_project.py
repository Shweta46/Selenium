from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)

s = driver.find_element(By.NAME, 'q')
s.send_keys('Coursera')
s.send_keys(Keys.RETURN)
driver.find_element(By.LINK_TEXT, "Login").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, '//button[@class="_d6ddka css-1wn7qwq" and @data-track-component="continue_with_google_auth_btn"]').click()
driver.implicitly_wait(10)

