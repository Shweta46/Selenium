import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://testsigma.com/blog/python-selenium-example/")
print(driver.title)
# search = driver.find_element(By.NAME, 'q')
# search.send_keys('testing in python using selenium')
# search.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

# explicit wait in selenium
try:
    main = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "main"))
    )
    # find_element is different from find_elements
    headers = main.find_elements(By.TAG_NAME, "h2")
    print(type(headers))
    for header in headers:
        print(header.text)
finally:
    driver.quit()

driver.quit()
