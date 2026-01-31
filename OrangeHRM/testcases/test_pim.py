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


       first_name = "Alannn"
       last_name = "Doe"


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


       first_name = "Alannn"
       last_name = "Doe"


       # Delete employee directly
       deleted = pim.delete_employee(first_name, last_name)
       assert deleted is True, f"Employee {first_name} {last_name} should be deleted successfully"


       # Verify employee no longer exists
       assert pim.search_employee(first_name,
                                  last_name) is False, f"Employee {first_name} {last_name} should not be found after deletion"

   def test_add_employee_with_login(self):
       pim = PimPage(self.driver, self.wait)
       login = LoginPage(self.driver, self.wait)

       # Fixed employee info
       first_name = "Albert"
       last_name = "Tester"
       emp_id = "978761"
       username = "albert096"
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

       # Step 5: Wait for dashboard as the new employee
       DASHBOARD_HEADER = (By.XPATH, "//h6[contains(text(),'Dashboard')]")
       dashboard_visible = WaitUtils.wait_for_visibility(self.wait, DASHBOARD_HEADER)

      # assert dashboard_visible, "New employee should log in successfully"
