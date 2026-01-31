import pytest
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.leave_page import LeavePage
from Config.conftest import setup_class


@pytest.mark.usefixtures("setup_class")
class TestLeave:

    def test_entitlement_and_assign_leave(self):
        login = LoginPage(self.driver, self.wait)
        pim = PimPage(self.driver, self.wait)
        leave = LeavePage(self.driver, self.wait)

        login.login("Admin", "admin123")

        first_name = "Alann"
        last_name = "Doe"
        full_name = f"{first_name} {last_name}"

        pim.add_employee(first_name, last_name)

        leave.add_entitlement(full_name, "CAN - Vacation", 50)
        leave.assign_leave(full_name, "CAN - Vacation", "2026-02-10", "2026-02-12", "Test leave")