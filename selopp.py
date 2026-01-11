import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class selenium:
    def __init__(self):
        options = Options()  # Initialize Chrome options
        # Open Chrome in guest mode
        options.add_argument('--guest')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.btnLogin = '//input[@id="login-button"]'
        self.username= '//input[@id="user-name"]'
        self.password = '//input[@id="password"]'
        self.text = '//div[@class="login_logo"]'
        self.product1 ='//button[@id="add-to-cart-sauce-labs-backpack"]'
        self.product2 ='//button[@id="add-to-cart-sauce-labs-bike-light"]'
        self.p2remove = '//button[@id="remove-sauce-labs-bike-light"]'
        self.p1heading = '//*[@id="item_4_title_link"]/div'
        self.BackProducts ='//button[@id="back-to-products"]'
        self.dropdown = '//*[@id="header_container"]/div[2]/div/span/select'
        self.carticon = '//*[@id="shopping_cart_container"]/a'
        self.ContinueShopping = '//button[@id="continue-shopping"]'
        self.checkout = '//button[@id="checkout"]'
        self.F_name = '//*[@id="first-name"]'
        self.L_name = '//*[@id="last-name"]'
        self.P_Code = '//*[@id="postal-code"]'
        self.btnCheck = '//*[@id="continue"]'
        self.FP_Price = '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div'
        self.SF_Price = '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div'
        self.TotalProduct = '//*[@id="checkout_summary_container"]/div/div[2]/div[6]'
        self.tax = '//*[@id="checkout_summary_container"]/div/div[2]/div[7]'


    def get(self,url):
        self.driver.get(url=url)

    def click(self):
        self.driver.find_element(By.XPATH,self.btnLogin).click()

    def sendKeys(self):
        self.driver.find_element(By.XPATH,self.username).send_keys("standard_user")
        self.driver.find_element(By.XPATH,self.password).send_keys("secret_sauce")

    def heading(self):
        headingcheck = self.driver.find_element(By.XPATH, self.text).text
        print(headingcheck)
        assert headingcheck == "Swag Labs"
        print("Test passed")

    def AddProductToCart(self):
        self.driver.find_element(By.XPATH,self.product1).click()
        self.driver.find_element(By.XPATH,self.product2).click()

    def RemoveProductFromCart(self):
        self.driver.find_element(By.XPATH,self.p2remove).click()

    def FirstProductHeading(self):
        self.driver.find_element(By.XPATH,self.p1heading).click()

    def BackToProducts(self):
        self.driver.find_element(By.XPATH,self.BackProducts).click()

    def FilterDropdown(self):
        # Locate the dropdown element (DO NOT click)
        dropdownelement = self.driver.find_element(By.XPATH, self.dropdown)

        # Create Select object
        select = Select(dropdownelement)

        # Select option by index (2 = third option)
        select.select_by_index(2)

        # Optional wait to see selection
        time.sleep(3)

    def IconCart(self):
        self.driver.find_element(By.XPATH,self.carticon).click()

    def ConShopping(self):
        self.driver.find_element(By.XPATH,self.ContinueShopping).click()

    def Checkout(self):
        self.driver.find_element(By.XPATH,self.checkout).click()

    def CheckoutDetails(self):
        self.driver.find_element(By.XPATH,self.F_name).send_keys("ALEENA")
        self.driver.find_element(By.XPATH,self.L_name).send_keys("IQBAL")
        self.driver.find_element(By.XPATH,self.P_Code).send_keys("123456")

    def ContinueCheckout(self):
        self.driver.find_element(By.XPATH,self.btnCheck).click()

    def GetProductPrice (self):
        price1 = self.driver.find_element(By.XPATH, self.FP_Price).text
        print(price1)
        newprice1 =price1.replace("$","")
        print(newprice1)
        priceFloat =float(newprice1)
        print(priceFloat)

        price2 = self.driver.find_element(By.XPATH, self.SF_Price).text
        print(price2)
        newprice2 = price2.replace("$", "")
        print(newprice2)
        priceFloat2 = float(newprice2)
        print(priceFloat2)
        SumOfProductPrice = priceFloat +priceFloat2
        print(SumOfProductPrice)

        totalItem = self.driver.find_element(By.XPATH, self.TotalProduct).text
        ui_total = totalItem.replace("Item total: $", "")
        ui_total = float(ui_total)
        print("UI Total:", ui_total)
        print(totalItem)
        time.sleep(3)


        assert SumOfProductPrice == ui_total
        print("TEST PASSED ")

        tax = round(ui_total * 0.08, 2)
        print("Calculated Tax:", tax)

        tax_text = self.driver.find_element(By.XPATH, self.tax).text
        print("UI TAX TEXT: ", tax_text)

        ui_tax = float(tax_text.replace("Tax: $", ""))
        print("UI TAX:", ui_tax)
        if round(tax, 2) == round(ui_tax, 2):
            print("PASSED")
        else:
            print("FAILED")
        time.sleep(3)



obj = selenium()
obj.get("https://www.saucedemo.com/")
obj.heading()
obj.sendKeys()
obj.click()
time.sleep(3)
obj.AddProductToCart()
time.sleep(3)
"""obj.RemoveProductFromCart()
time.sleep(3)"""
obj.FirstProductHeading()
time.sleep(3)
obj.BackToProducts()
time.sleep(3)
obj.FilterDropdown()
time.sleep(3)
obj.IconCart()

#obj.ConShopping()

obj.Checkout()

obj.CheckoutDetails()
obj.ContinueCheckout()
time.sleep(3)

obj.GetProductPrice()