# pages/pim_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from utils.wait_utils import WaitUtils


class PimPage:
   # -------------------- LOCATORS --------------------
   PIM_TAB = (By.XPATH, "//span[text()='PIM']")
   ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
   EMP_LIST = (By.XPATH, "//a[normalize-space()='Employee List']")
   FIRST_NAME = (By.XPATH, "//input[@name='firstName']")
   LAST_NAME = (By.XPATH, "//input[@name='lastName']")
   EMP_ID = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
   SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
   SEARCH_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
   SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
   TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-card']//div[@class='oxd-table-row oxd-table-row--with-border']")
   CHECKBOX = (By.XPATH, "//i[contains(@class,'oxd-checkbox-input-icon')]")
   DELETE_BUTTON = (By.XPATH, "//button[contains(@class,'oxd-button--label-danger')]")
   CONFIRM_DELETE = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
   LOADER = (By.XPATH, "//div[contains(@class,'oxd-form-loader')]")
   TABLE_ROWS = (By.XPATH, "//div[@class='oxd-table-body']//div[contains(@class,'oxd-table-row')]")
   LOGIN_TOGGLE = (By.XPATH, "//span[contains(@class,'oxd-switch-input')]")


   def __init__(self, driver, wait):
       self.driver = driver
       self.wait = wait


   # -------------------- HELPER --------------------
   def safe_click(self, locator, retries=3):
       """Try clicking an element, retrying if a loader intercepts the click."""
       for attempt in range(retries):
           try:
               WaitUtils.wait_for_clickable(self.wait, locator).click()
               return True
           except ElementClickInterceptedException:
               WaitUtils.wait_for_invisibility(self.wait, self.LOADER)
       return False


   # -------------------- ACTION METHODS --------------------
   def navigate_to_pim(self):
       self.safe_click(self.PIM_TAB)


   def add_employee(self, first_name, last_name, emp_id=None):
       self.navigate_to_pim()
       self.safe_click(self.ADD_BUTTON)


       # Fill mandatory fields
       WaitUtils.wait_for_visibility(self.wait, self.FIRST_NAME).send_keys(first_name)
       WaitUtils.wait_for_visibility(self.wait, self.LAST_NAME).send_keys(last_name)


       if emp_id:
           emp = WaitUtils.wait_for_visibility(self.wait, self.EMP_ID)
           emp.send_keys(Keys.CONTROL, "a")
           emp.send_keys(Keys.BACKSPACE)
           emp.send_keys(emp_id)


       # Save employee
       self.safe_click(self.SAVE_BUTTON)


       # ✅ Wait for Personal Details page to confirm employee creation
       PERSONAL_DETAILS_HEADER = (By.XPATH, "//h6[normalize-space()='Personal Details']")
       WaitUtils.wait_for_visibility(self.wait, PERSONAL_DETAILS_HEADER)


       # Navigate back to Employee List
       self.safe_click(self.EMP_LIST)
       WaitUtils.wait_for_invisibility(self.wait, self.LOADER)


   def add_employee_with_credentials(self, first_name, last_name, emp_id=None, username=None, password=None):
       self.navigate_to_pim()
       self.safe_click(self.ADD_BUTTON)


       # Fill mandatory fields
       WaitUtils.wait_for_visibility(self.wait, self.FIRST_NAME).send_keys(first_name)
       WaitUtils.wait_for_visibility(self.wait, self.LAST_NAME).send_keys(last_name)


       if emp_id:
           emp = WaitUtils.wait_for_visibility(self.wait, self.EMP_ID)
           emp.send_keys(Keys.CONTROL, "a")
           emp.send_keys(Keys.BACKSPACE)
           emp.send_keys(emp_id)


       # ✅ Toggle "Create Login Details"
       LOGIN_TOGGLE = (By.XPATH, "//span[contains(@class,'oxd-switch-input')]")
       WaitUtils.wait_for_clickable(self.wait, LOGIN_TOGGLE).click()


       # ✅ Use your provided XPaths for login fields
       USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/following::input[1]")
       PASSWORD_INPUT = (By.XPATH, '(//input[@type="password"])[1]')
       CONFIRM_PASSWORD_INPUT = (By.XPATH, '(//input[@type="password"])[2]')


       # Wait for login fields to appear before typing
       WaitUtils.wait_for_visibility(self.wait, USERNAME_INPUT).send_keys(username)
       WaitUtils.wait_for_visibility(self.wait, PASSWORD_INPUT).send_keys(password)
       WaitUtils.wait_for_visibility(self.wait, CONFIRM_PASSWORD_INPUT).send_keys(password)


       # Save employee
       self.safe_click(self.SAVE_BUTTON)


       # ✅ Wait for Personal Details page to confirm employee creation
       PERSONAL_DETAILS_HEADER = (By.XPATH, "//h6[text()='Personal Details']")
       WaitUtils.wait_for_visibility(self.wait, PERSONAL_DETAILS_HEADER)


       return username, password


   def search_employee(self, first_name, last_name):
       self.navigate_to_pim()
       self.safe_click(self.EMP_LIST)


       search_box = WaitUtils.wait_for_visibility(self.wait, self.SEARCH_NAME)
       search_box.clear()
       search_box.send_keys(first_name + " " + last_name)
       self.safe_click(self.SEARCH_BUTTON)


       WaitUtils.wait_for_invisibility(self.wait, self.LOADER)


       import time
       for attempt in range(5):  # retry up to 5 times
           try:
               rows = self.driver.find_elements(*self.TABLE_ROWS)
               for row in rows:
                   text = row.text
                   if first_name in text and last_name in text:
                       return True
           except StaleElementReferenceException:
               # Table refreshed, retry
               pass
           time.sleep(2)


       return False


   def delete_employee(self, first_name, last_name):
       self.navigate_to_pim()
       self.safe_click(self.EMP_LIST)


       # Search by first name only (OrangeHRM usually matches this)
       search_box = WaitUtils.wait_for_visibility(self.wait, self.SEARCH_NAME)
       search_box.clear()
       search_box.send_keys(first_name)
       self.safe_click(self.SEARCH_BUTTON)


       # Wait until loader disappears
       WaitUtils.wait_for_invisibility(self.wait, self.LOADER)


       import time
       for attempt in range(5):  # retry loop
           rows = self.driver.find_elements(*self.TABLE_ROWS)
           for row in rows:
               text = row.text
               if first_name in text and last_name in text:
                   # ✅ Find checkbox inside the correct row
                   checkbox = row.find_element(By.XPATH, ".//i[contains(@class,'oxd-checkbox-input-icon')]")
                   checkbox.click()


                   # Delete and confirm
                   self.safe_click(self.DELETE_BUTTON)
                   self.safe_click(self.CONFIRM_DELETE)
                   WaitUtils.wait_for_invisibility(self.wait, self.LOADER)
                   return True
           time.sleep(2)


       return False
