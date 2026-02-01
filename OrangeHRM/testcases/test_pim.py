import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.pim_page import PimPage
from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from Config.conftest import setup_class # explicit import


@pytest.mark.usefixtures("setup_class")
class TestPIM:


   def test_add_and_search_employee(self):
       login = LoginPage(self.driver, self.wait)
       pim = PimPage(self.driver, self.wait)


       login.refresh_page()
       login.login("Admin", "admin123")


       first_name = "Danee"
       last_name = "Bradd"


       pim.add_employee(first_name, last_name)


       pim.search_employee(first_name, last_name)


   def test_delete_employee(self):
       # login = LoginPage(self.driver, self.wait)
       # pim = PimPage(self.driver, self.wait)


       # --- Option 1: Fresh login (commented out) ---
       # login.refresh_page()
       # login.login("Admin", "admin123")


       # --- Option 2: Reuse session (active) ---
       pim = PimPage(self.driver, self.wait)


       first_name = "Danee"
       last_name = "Bradd"


       # Delete employee directly
       deleted = pim.delete_employee(first_name, last_name)
       assert deleted is True, f"Employee {first_name} {last_name} should be deleted successfully"


       # Verify employee no longer exists
       assert pim.search_employee(first_name,last_name) is False, f"Employee {first_name} {last_name} should not be found after deletion"

   def test_add_employee_with_login(self):
       pim = PimPage(self.driver, self.wait)
       login = LoginPage(self.driver, self.wait)

       # Fixed employee info
       first_name = "Albertt"
       last_name = "Tester"
       emp_id = "093763"
       username = "alberttester727"
       password = "Pass@123"

       # Step 1: Add employee with credentials
       username_created, password_created = pim.add_employee_with_credentials(
           first_name=first_name,
           last_name=last_name,
           emp_id=emp_id,
           username=username,
           password=password
       )

       # Step 2: Navigate to Dashboard as Admin
       DASHBOARD_TAB = (By.XPATH, "//span[text()='Dashboard']")
       WaitUtils.wait_for_clickable(self.wait, DASHBOARD_TAB).click()

       # Step 3: Logout as Admin
       login.logout()

       # Step 4: Login with new employee credentials
       login.login(username=username_created, password=password_created)

       # 🛑 WAIT FOR GLOBAL LOADER TO DISAPPEAR
       WaitUtils.wait_for_invisibility(self.wait, pim.LOADER)

       # Step 5: Verify login by checking user dropdown
       # Step 5: Verify login success
       self.wait.until(lambda d: "auth/login" not in d.current_url)
       assert "auth/login" not in self.driver.current_url


