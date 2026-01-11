import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# -------------------- XPATH Declarations --------------------
ViewProductBtn = '//a[text()="View all products"]'
Product1 = '(//span[text()="View details"])[1]'
Product2 = '(//span[text()="View details"])[2]'
Product3 = '(//span[text()="View details"])[3]'
CheckStock = '//button[text()="Check stock"]'
Store = '//select[@name="storeId"]'
QTY = '//select[@name="quantity"]'
AddToCart = '//button[text()="Add to cart"]'
ViewCart = '//a[text()="View cart"]'
Desc = '/html/body/div[2]/section/div/section/div[2]/span[2]/p[1]/text()'
ChkQty='//form[@action="/catalog/cart"]/select'

# -------------------- Driver Setup --------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ginandjuice.shop/")
driver.implicitly_wait(60)

# -------------------- Navigate to Product --------------------
V1 = driver.find_element(By.XPATH, ViewProductBtn)
driver.execute_script("arguments[0].scrollIntoView(true);", V1)
V1.click()

v2 = driver.find_element(By.XPATH, Product1)
driver.execute_script("arguments[0].scrollIntoView(true);", v2)
v2.click()
driver.execute_script("window.scrollTo(0,500);")

# -------------------- Check Stock --------------------
driver.find_element(By.XPATH, CheckStock).click()
time.sleep(2)
St1 = driver.find_element(By.XPATH, '//span[@id="stockCheckResult"]').text
St1 = St1.replace('units', "")
print('Stock available:', St1)

# -------------------- Validate Description --------------------
expected_desc = (
    "Originally a limited edition prototype, but back by popular demand, "
    "and now premixed with premium fruit juice, Pineapple Edition Gin is sure to rock your world. "
    "What doesn't taste better with a little pineapple added? Pizza? We'll let you fight that one out for yourselves. "
    "We think the gin is pretty good though."
)
descChck = driver.find_element(By.XPATH, '//span[@class="description"]/p').text
print('Product description:', descChck)
assert descChck == expected_desc, "Description does not match!"

# -------------------- Get Price and Calculate --------------------
pricex1 = driver.find_element(By.XPATH, '/html/body/div[2]/section/div/section/div[2]/span[1]/span').text
print('Price text:', pricex1)
pricex1 = float(pricex1.replace('$', ""))
print('Price value:', pricex1)

qtychchk = pricex1 * 5
print('Calculated total for 5 units:', qtychchk)

# -------------------- Select Quantity and Add to Cart --------------------
select_qty = Select(driver.find_element(By.NAME, "quantity"))
select_qty.select_by_visible_text("5")
time.sleep(2)

driver.find_element(By.XPATH, AddToCart).click()
driver.find_element(By.XPATH, ViewCart).click()
time.sleep(2)

# -------------------- Validate Checkout Price --------------------
ChkoutP = driver.find_element(By.XPATH, "//div[@class='cart-order-section']//strong").text
ChkoutP = float(ChkoutP.replace('$', ""))
print('Checkout price:', ChkoutP)

assert ChkoutP == qtychchk, "Checkout price does not match calculated price!"
print("Assertion passed: Checkout price matches the calculated price")

# -------------------- Changing qty to 1 on checkout page--------------------
select2=Select(driver.find_element(By.XPATH,ChkQty))
select2.select_by_visible_text("1")
time.sleep(9)
ChkoutP = driver.find_element(By.XPATH, "//div[@class='cart-order-section']//strong").text
ChkoutP = float(ChkoutP.replace('$', ""))
print('price of QTYx1  on Checkout   :', ChkoutP)
assert ChkoutP == pricex1
print("Price of x1 matches; Assertion passed")

# -------------------- validating the Url of Checkout--------------------
CUrl=driver.current_url
assert CUrl=="https://ginandjuice.shop/catalog/cart"
print("Current URL Assertion passed")

