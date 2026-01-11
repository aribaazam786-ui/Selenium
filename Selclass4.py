import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

options=Options()
options.add_argument('--incognito')
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
#Login
driver.find_element(By.CSS_SELECTOR,'#user-name').send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,'[placeholder="Password"]').send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR,"#login-button").click()
time.sleep(4)
#dropdown usage
dropdown=driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select')
dd=Select(dropdown)
dd.select_by_visible_text("Name (A to Z)")
time.sleep(5)
#Add Product
driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-backpack"]').click()
Price=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div').text
#Saving price value and replacing the $
print(Price)
Price = Price.replace('$', "")
p=float(Price)
print(p)
#Product2
driver.find_element(By.XPATH,'//button[@name="add-to-cart-sauce-labs-bike-light"]').click()
Price1=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div').text
print(Price1)
Price1 = Price1.replace('$', "")
p1=float(Price1)
print(p1)
#Product3
driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
Price2=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div').text
print(Price2)
Price2 = Price2.replace('$', "")
p2=float(Price2)
print(p2)
time.sleep(3)
#Click on Continue Shopping (Back to Product page)
driver.find_element(By.CSS_SELECTOR,'[class="shopping_cart_link"]').click()
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)
#Product4
driver.find_element(By.XPATH,'//button[@id="continue-shopping"]').click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,400);")
driver.find_element(By.XPATH,'//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
Price3=driver.find_element(By.XPATH,'//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div').text
print(Price3)
Price3 = Price3.replace('$', "")
p3=float(Price3)
print(p3)
time.sleep(3)
#Total of the selected products
Total=p+p1+p2+p3
print('Manual total of the selected product',Total)
driver.execute_script("window.scrollTo(400,0);")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,'[class="shopping_cart_link"]').click()
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
#Checkout button click
driver.find_element(By.XPATH,'//button[@name="checkout"]').click()
time.sleep(5)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
#Checkout page info input
driver.find_element(By.XPATH,'//*[@id="first-name"]').send_keys("Albert")
driver.find_element(By.XPATH,'//*[@id="last-name"]').send_keys("Smith")
driver.find_element(By.XPATH,'//*[@id="postal-code"]').send_keys("123456")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="continue"]').click()
time.sleep(5)
#Item total from the checkout page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
Itemtotal=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[6]').text
Itemtotal = Itemtotal.replace('Item total: $', "")
total=float(Itemtotal)
print('Total appearing on checkout',total)
assert total == Total
time.sleep(3)
driver.find_element(By.XPATH,'//button[@id="finish"]').click()
print(driver.current_url)
time.sleep(5)