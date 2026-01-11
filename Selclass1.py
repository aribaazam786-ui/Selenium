import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #to access Chrome options

from Selclass2 import driver

options=Options()
"""options.add_argument('--incognito') #add_argument method for incognito or any other options
options.add_argument('--headless') #headless to run the instruction in background without UI
print("Navigating to web")
driver = webdriver.Chrome(options=options) #should pass options here for chrome access
print("Navigated to web")
driver.get('http://ginandjuice.shop') #get is used to open browser
time.sleep(3)"""

driver.execute_script("window.open('https://ginandjuice.shop','_blank');")
time.sleep(3)
