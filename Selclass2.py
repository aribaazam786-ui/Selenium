import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('incognito')

driver = webdriver.Chrome(options=options)
driver.get("https://ginandjuice.shop/")
time.sleep(5)
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.open('https://ginandjuice.shop/','_blank');") #to open in new tab
time.sleep(5)
driver.execute_script("window.open('https://www.google.com/','_blank');") #to open in new tab
time.sleep(5)
driver.execute_script("window.open('https://facebook.com/','_blank');") #to open in new tab
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.execute_script("window.scrollTo(0,800);")
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
time.sleep(3)
driver.minimize_window()
time.sleep(2)