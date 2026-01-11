import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


#------Declaring XPaths------------
ViewAllProducts='//a[text()="View all products"]'
Product2='(//span[text()="View details"])[2]'
Store='//select[@name="storeId"]'
ChckStock='//button[text()="Check stock"]'
Qty='//select[@name="quantity"]'
AddToCart='//button[text()="Add to cart"]'
CartIcon='//a[@class="cart-icon"]'
Pricex1='//span[@class="price"]'
CHKP="//div[@class='cart-order-section']//strong"

# -------------------- Driver Setup --------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ginandjuice.shop/")
wait=WebDriverWait(driver,50)

# -------------------- Navigate to Product --------------------
V1 = wait.until(EC.visibility_of_element_located((By.XPATH, ViewAllProducts)))
driver.execute_script("arguments[0].scrollIntoView(true);", V1)
V1.click()

V2=wait.until(EC.visibility_of_element_located((By.XPATH, Product2)))
driver.execute_script("arguments[0].scrollIntoView(true);", V2)
V2.click()

#___________Saving value of single product
RetailP=wait.until(EC.visibility_of_element_located((By.XPATH, Pricex1))).text
RetailP = float(RetailP.replace('$', ''))
print('Retail price:', RetailP)

# -------------------- Selecting Store and Qty --------------------
qty_dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, Qty))
)
select_qty = Select(qty_dropdown)
select_qty.select_by_visible_text("5")
driver.find_element(By.XPATH, AddToCart).click()
#selecting Paris
store_paris=wait.until(
   EC.presence_of_element_located((By.XPATH,Store))
)
driver.execute_script("arguments[0].scrollIntoView(true);", store_paris)
select_store1 = Select(store_paris)
select_store1.select_by_visible_text("Paris")
qty_dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, Qty))
)
select_qty1 = Select(qty_dropdown)
select_qty1.select_by_visible_text("6")
driver.find_element(By.XPATH, AddToCart).click()
#Selecting Milan
store_milan=wait.until(
    EC.presence_of_element_located((By.XPATH,Store))
)
driver.execute_script("arguments[0].scrollIntoView(true);", store_milan)
select_store2 = Select(store_milan)
select_store2.select_by_visible_text("Milan")
qty_dropdown = wait.until(
    EC.element_to_be_clickable((By.XPATH, Qty))
)
select_qty2 = Select(qty_dropdown)
select_qty2.select_by_visible_text("3")
driver.find_element(By.XPATH, AddToCart).click()

#_____________Cart Icon click
time.sleep(2)
cartIcon = wait.until(EC.element_to_be_clickable((By.XPATH, CartIcon)))
driver.execute_script("arguments[0].scrollIntoView(true);", cartIcon)
cartIcon.click()


#________________CHECKOUT-------------
TotalQty=5+6+3
TotalPrice=round(float(TotalQty*RetailP),2)
print('Total price:', TotalPrice)
#----------match with price on checkout page
ChkPrice=wait.until(EC.visibility_of_element_located((By.XPATH,CHKP)))
driver.execute_script("arguments[0].scrollIntoView(true);", ChkPrice)
ChkPrice=ChkPrice.text
ChkPrice = float(ChkPrice.replace('$', ''))
print('Checkout price:', ChkPrice)

assert ChkPrice == TotalPrice
print("Assertion Passed")