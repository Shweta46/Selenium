import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Installed selenium
# Downloaded and installed Chrome driver and then selecting the path for that
# then, find function, and then By function in the webdriver
# .click()
# send_keys()
# selectors like name, id, and class_name
# css selector instead of class_name is the class name has whitespaces in the middle
# XPath and how to access that using the inspect method in the browser

driver = webdriver.Chrome()
driver.get("http://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds

driver.find_element(By.NAME, "username").send_keys("Admin")

driver.find_element(By.NAME, "password").send_keys("admin123")
#
driver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
#
actual_title = driver.title
expected_title = 'OrangeHRM'
# if expected_title == actual_title:
#     print("Login test passed.")
# else:
#     print('Login test failed.')
print(actual_title)
assert expected_title == actual_title, 'Not passed.'

driver.close()

'''
1. 
XPath in here:
In the below expression, we have taken the “text” of the link as an attribute and ‘here’ as a partial value as shown in the below screenshot. 
This will find the link (‘here’) as it displays the text ‘here’.
Xpath=//*[contains(text(),'here')]
Xpath=//*[contains(@href,'guru99.com')]

2. 
In XPath, the `*` is a wildcard that matches any element node. So, in the expression `//*[@class='barone']`, the `*` is used to select any element in the XML or HTML document that has a class attribute with the value `'barone'`.

Here's a breakdown of the expression:
- `//`: Selects nodes in the document from the current node that match the selection no matter where they are.
- `*`: Selects all element nodes.
- `[@class='barone']`: Selects elements with a class attribute equal to `'barone'`.

So, overall, the XPath expression `//*[@class='barone']` selects all elements in the document that have a class attribute with the value `'barone'`.

3. Xpath=//td[text()='UserID']
In this expression, with text function, we find the element with exact text match as shown below. In our case, we find the element with text “UserID”.




'''
