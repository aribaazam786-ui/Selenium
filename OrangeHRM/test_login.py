import pytest
import pytest_check as check
from pages.login_page import LoginPage
from Config.conftest import setup_class # explicit import
from utils.wait_utils import WaitUtils



@pytest.mark.usefixtures("setup_class")
class TestLogin:


   def test_empty_password(self):
       login_page = LoginPage(self.driver, self.wait)
       login_page.refresh_page()
       login_page.enter_username("Admin")
       login_page.click_login()
       # Wait for the "Required" message to appear
       error_element = WaitUtils.wait_for_visibility(self.wait, login_page.PASS_REQUIRED)
       error_text = error_element.text

       check.equal(error_text, "Required", "Empty password should show 'Required'")


   def test_empty_username(self):
       login_page = LoginPage(self.driver, self.wait)
       login_page.refresh_page()
       login_page.enter_password("admin123")
       login_page.click_login()
       error_element = WaitUtils.wait_for_visibility(self.wait, login_page.UNAME_REQUIRED)
       error_text = error_element.text
       check.equal(error_text, "Required", "Empty password should show 'Required'")


   def test_incorrect_credentials(self):
       login_page = LoginPage(self.driver, self.wait)
       login_page.refresh_page()
       login_page.login("Admin434", "admin124343")
       error_element = WaitUtils.wait_for_visibility(self.wait, login_page.INVALID_CRED_ALERT)
       error_text = error_element.text
       check.equal(error_text, "Invalid credentials", "Empty password should show 'Required'")


   def test_wrong_password(self):
       login_page = LoginPage(self.driver, self.wait)
       login_page.refresh_page()
       login_page.login("Admin", "wrongpass123")
       error_element = WaitUtils.wait_for_visibility(self.wait, login_page.INVALID_CRED_ALERT)
       error_text = error_element.text
       check.equal(error_text, "Invalid credentials", "Empty password should show 'Required'")


   def test_wrong_username(self):
       login_page = LoginPage(self.driver, self.wait)
       login_page.refresh_page()
       login_page.login("wronguser", "admin123")
       error_element = WaitUtils.wait_for_visibility(self.wait, login_page.INVALID_CRED_ALERT)
       error_text = error_element.text
       check.equal(error_text, "Invalid credentials", "Empty password should show 'Required'")


   def test_successful_login(self):
       login_page = LoginPage(self.driver, self.wait)
       login_page.refresh_page()
       login_page.login("Admin", "admin123")
       expected = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
       actual = login_page.get_current_url()
       check.equal(actual, expected, f"Expected dashboard URL but got: {actual}")