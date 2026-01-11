import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class GinandJuice:
    def __init__(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

        self.Products='//a[contains(.,"Products")]'
        self.blog='//a[contains(.,"Blog")]'
        self.ourstory='(//a[contains(.,"Our story")][1])'
        self.cart='//a[@class="cart-icon"]'
        self.acc='//*[@id="scanMeHeader"]/section[2]/div/div/nav/ul[2]/li[1]/a'

        self.Accesories='//a[contains(.,"Accessories")]'
        self.Accompaniments='//a[contains(.,"Accompaniments")]'
        self.Books='//a[contains(.,"Books")]'
        self.Gin='//a[contains(.,"Gin")]'
        self.Juice='//a[contains(.,"Juice")]'
        self.Blog1='//a[@href="/blog/post?postId=3"]/img'
        self.blog2='//a[@href="/blog/post?postId=4"]/img'

    def Homepage(self):
        self.driver.find_element(By.XPATH, self.Products).click()
        self.driver.find_element(By.XPATH, self.blog).click()
        self.driver.find_element(By.XPATH, self.ourstory).click()
       # self.driver.find_element(By.XPATH, self.cart).click()
       # self.driver.find_element(By.XPATH, self.acc).click()

    def ProductsPage(self):
        self.driver.find_element(By.XPATH, self.Products).click()
        self.driver.find_element(By.XPATH, self.Accesories).click()
        self.driver.find_element(By.XPATH, self.Accompaniments).click()
        self.driver.find_element(By.XPATH, self.Books).click()
        self.driver.find_element(By.XPATH, self.Gin).click()
        self.driver.find_element(By.XPATH, self.Juice).click()

    def blogPage(self):
        self.driver.find_element(By.XPATH, self.blog).click()
        self.driver.find_element(By.XPATH, self.Blog1).click()
        self.driver.find_element(By.XPATH, self.blog).click()
        self.driver.find_element(By.XPATH, self.blog2).click()
    def ourstorypage(self):
        self.driver.find_element(By.XPATH, self.ourstory).click()
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')



# -------- Run test --------
obj = GinandJuice()
obj.driver.get("https://ginandjuice.shop/")
obj.Homepage()
obj.ProductsPage()
obj.blogPage()
obj.ourstorypage()
time.sleep(3)
