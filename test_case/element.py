from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver:driver.find_element(By.NAME, self.locator))
        driver.find_element(By.NAME, self.locator).clear()
        river.find_element(By.NAME,
                           self.locator).send.keys(value)
