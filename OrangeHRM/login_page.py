# pages/login_page.py
from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils


class LoginPage:
   # Locators
   USERNAME_INPUT = (By.XPATH, '//input[@name="username"]')
   PASSWORD_INPUT = (By.XPATH, '//input[@name="password"]')
   LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
   UNAME_REQUIRED = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span')
   PASS_REQUIRED = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span')
   INVALID_CRED_ALERT = (By.XPATH, "//div[@role='alert']")
   DASHBOARD = (By.XPATH, "//h6[text()='Dashboard']")
   USER_MENU = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
   LOGOUT = (By.XPATH, "//a[text()='Logout']")


   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait


   def enter_username(self, username):
       field = WaitUtils.wait_for_visibility(self.wait, self.USERNAME_INPUT)
       field.clear()
       field.send_keys(username)


   def enter_password(self, password):
       field = WaitUtils.wait_for_visibility(self.wait, self.PASSWORD_INPUT)
       field.clear()
       field.send_keys(password)


   def click_login(self):
       WaitUtils.wait_for_clickable(self.wait, self.LOGIN_BUTTON).click()


   def login(self, username, password):
       self.enter_username(username)
       self.enter_password(password)
       self.click_login()
       # Wait for dashboard if login is successful
       try:
           WaitUtils.wait_for_visibility(self.wait, self.DASHBOARD)
       except:
           pass


   def get_current_url(self):
       return self.driver.current_url


   def get_required_error_message(self):
       elem = WaitUtils.wait_for_visibility(self.wait, (By.XPATH, "//span[contains(text(),'Required')]"))
       return elem.text.strip()


   def get_invalid_credentials_message(self):
       elem = WaitUtils.wait_for_visibility(self.wait, self.INVALID_CRED_ALERT)
       return elem.text.strip()


   def is_invalid_credentials_displayed(self):
       elem = WaitUtils.wait_for_visibility(self.wait, self.INVALID_CRED_ALERT)
       return elem.is_displayed()


   def refresh_page(self):
       self.driver.refresh()
       WaitUtils.wait_for_visibility(self.wait, self.USERNAME_INPUT)


   def logout(self):
       WaitUtils.wait_for_clickable(self.wait, self.USER_MENU).click()
       WaitUtils.wait_for_clickable(self.wait, self.LOGOUT).click()
       WaitUtils.wait_for_visibility(self.wait, self.USERNAME_INPUT)
