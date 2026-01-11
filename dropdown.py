import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(3)

# Locate the <select> element
dropdown = driver.find_element(By.ID, "dropdown")

# Use Select class
dd = Select(dropdown)
dd.select_by_index(1)   # Option 1
time.sleep(3)
dd.select_by_visible_text("Option 1")
dd.select_by_value("1")
driver.save_screenshot('tutorialspoint.png')


time.sleep(10)