import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.support.select import Select

#------Declaring XPaths------------
ViewAllProducts='//a[text()="View all products"]'
Product1='(//span[text()="View details"])[1]'
Store='//select[@name="storeId"]'
ChckStock='//button[text()="Check stock"]'
Qty='//select[@name="quantity"]'
AddToCart='//button[text()="Add to cart"]'
CartIcon='//a[@class="cart-icon"]'
Pricex1='//span[@class="price"]'

# -------------------- Driver Setup --------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ginandjuice.shop/")
driver.implicitly_wait(60)

# -------------------- Navigate to Product --------------------
V1 = driver.find_element(By.XPATH, ViewAllProducts)
driver.execute_script("arguments[0].scrollIntoView(true);", V1)
V1.click()

v2 = driver.find_element(By.XPATH, Product1)
driver.execute_script("arguments[0].scrollIntoView(true);", v2)
v2.click()
driver.execute_script("window.scrollTo(0,500);")
time.sleep(2)
# -------------------- Selecting Store and Qty --------------------
select_qty = Select(driver.find_element(By.XPATH,Qty))
select_qty.select_by_visible_text("5")
time.sleep(2)
driver.find_element(By.XPATH, AddToCart).click()
#selecting Paris
select_store = Select(driver.find_element(By.XPATH,Store))
select_store.select_by_visible_text("Paris")
select_qty = Select(driver.find_element(By.XPATH,Qty))
select_qty.select_by_visible_text("6")
time.sleep(2)
driver.find_element(By.XPATH, AddToCart).click()
time.sleep(2)
#Selecting Milan
select_store = Select(driver.find_element(By.XPATH,Store))
select_store.select_by_visible_text("Milan")
select_qty = Select(driver.find_element(By.XPATH,Qty))
select_qty.select_by_visible_text("4")
time.sleep(2)
driver.find_element(By.XPATH, AddToCart).click()
TotalQty=5+6+4
time.sleep(2)
#QTY on Icon
IconTxt=int(driver.find_element(By.XPATH, '//a[@class="cart-icon"]/span').text)
print('QTY on cart icon',IconTxt)
#----------Check if the selected Qty matches with Cart Icon
assert IconTxt==TotalQty,'Qty on cart icon should be equal to total Qty on cart icon'
print('Assertion Passed')
driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
time.sleep(3)

#----------------Match QTY on Checkout page
qty_dropdown = Select(driver.find_element(By.NAME, "quantity"))
selected_qty = qty_dropdown.first_selected_option.text

print("Selected quantity on checkout page:", selected_qty)
assert int(selected_qty)==  TotalQty
print('Assertion Passed')
#------------Checking price
Pricex1 = driver.find_element(By.XPATH, "//span[@class='item-price']").text
Pricex1 = float(Pricex1.replace('$', ''))

# Calculate expected total
TotalPrice = TotalQty * Pricex1

# Read checkout price
ChkoutP = driver.find_element(By.XPATH, "//div[@class='cart-order-section']//strong").text
ChkoutP = round(float(ChkoutP.replace('$', "")), 2)

print("Expected total:", TotalPrice)
print("Checkout price:", ChkoutP)

assert ChkoutP == TotalPrice, 'Checkout price should be equal to total price'
print('Assertion Passed')
