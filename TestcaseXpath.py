import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options=Options()
options.add_argument('--incognito')
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
#Testcase1 to check Header
Text=driver.find_element(By.CLASS_NAME,"login_logo").text
print(Text)
assert Text=="Swag Labs"
#Testcase2 Null submit Validation check
driver.find_element(By.XPATH, '//*[contains(@id,"login-button")]').click()
Val=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(Val)
time.sleep(3)
if Val=="Epic sadface: Username is required":
    print("Passed")
else:
    print("Failed")
#Testase3 Username Enter password validation
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('standard_user')
driver.find_element(By.XPATH, '//*[contains(@id,"login-button")]').click()
Val2=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(Val2)
time.sleep(3)
if Val2=="Epic sadface: Password is required":
    print("Passed")
else:
    print("Failed")
driver.refresh()
#Testase3 Password Enter username validation
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('secret_sauce')
driver.find_element(By.XPATH, '//*[contains(@id,"login-button")]').click()
Val3=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(Val3)
time.sleep(3)
if Val3=="Epic sadface: Username is required":
    print("Passed")
else:
    print("Failed")
driver.refresh()
#Testcase4
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('secret_sauce')
driver.find_element(By.XPATH, '//*[contains(@id,"login-button")]').click()
Val3=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(Val3)
time.sleep(3)
if Val3=="Epic sadface: Username is required":
    print("Passed")
else:
    print("Failed")
######
#Testcase4:wrong enter input validation
driver.refresh()
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('stand')
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('secret')
driver.find_element(By.XPATH, '//*[contains(@id,"login-button")]').click()
Val4=driver.find_element(By.CLASS_NAME,"error-message-container").text
print(Val4)
time.sleep(3)
if Val4=="Epic sadface: Username and password do not match any user in this service":
    print("Passed")
else:
    print("Failed")

