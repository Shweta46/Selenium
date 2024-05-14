from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(5)
# search_this = driver.find_element(By.NAME, 'q').send_keys('The Weekend Popular Lyrics')
# driver.find_element(By.XPATH, "//input[@value='Google Search']").click()
# search_this.send_keys(Keys.RETURN)

search_box = driver.find_element(By.NAME, 'q') # you are inside the element right now and are inside the search box so the operations performed later are inside this
search_box.send_keys('The Weekend Popular lyrics')
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(10)

name = (driver.find_element(By.XPATH, "//div[@aria-level='2' and @data-attrid='title']").text)
driver.implicitly_wait(5)
assert name == 'Popular', 'Not passed'

