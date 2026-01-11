import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
driver=webdriver.Chrome(options=options)
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(5)
element=driver.find_element(By.XPATH,'//h5[text()="Elements"]')
driver.execute_script("arguments[0].scrollIntoView(true);",element)
element.click()
driver.find_element(By.XPATH,'//span[text()="Text Box"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="userName"]').send_keys('tester')
driver.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys('abc@gmail.com')
driver.find_element(By.XPATH,'//*[@id="currentAddress"]').send_keys('this is test address')
driver.find_element(By.XPATH,'//*[@id="permanentAddress"]').send_keys('this is test address')
submit=driver.find_element(By.XPATH,'//*[@id="submit"]')
driver.execute_script("arguments[0].scrollIntoView(true);",submit)
submit.click()
time.sleep(2)
driver.find_element(By.XPATH,'//li[@id="item-1"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//span[text()="Home"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//li[@id="item-2"]').click()
time.sleep(5)
imp=driver.find_element(By.XPATH,'//label[text()="Impressive"]')
driver.execute_script("arguments[0].scrollIntoView(true);",imp)
imp.click()
time.sleep(5)
text=driver.find_element(By.XPATH,'//label[text()="Impressive"]').text
print(text)
assert text=="Impressive"
text2=driver.find_element(By.XPATH,'//span[@class="text-success"]').text
assert text2==text
driver.find_element(By.XPATH,'//span[text()="Web Tables"]').click()
time.sleep(2)
