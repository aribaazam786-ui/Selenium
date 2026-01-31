from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.wait_utils import WaitUtils


class LeavePage:

    # ===== LOCATORS =====
    LEAVE_TAB = (By.XPATH, "//a[@href='/web/index.php/leave/viewLeaveModule']")
    ENTITLEMENTS_MENU = (By.XPATH, "//span[normalize-space()='Entitlements']")
    EMPLOYEE_ENTITLEMENTS = (By.XPATH, "//a[normalize-space()='Employee Entitlements']")
    ASSIGN_LEAVE_MENU = (By.XPATH, "//a[normalize-space()='Assign Leave']")

    EMPLOYEE_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    SEARCH_BTN = (By.XPATH, "//button[@type='submit']")
    ADD_BTN = (By.XPATH, "//button[normalize-space()='Add']")
    LEAVE_TYPE_DROPDOWN = (By.XPATH, "//div[contains(@class,'oxd-select-text')]")
    ENTITLEMENT_DAYS_INPUT = (By.XPATH, "(//input[contains(@class,'oxd-input')])[2]")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    CONFIRM_BTN = (By.XPATH, "//button[normalize-space()='Confirm']")

    COMMENT_BOX = (By.XPATH, "//textarea[@placeholder='Type here']")

    # ✅ Exact date inputs for Assign Leave form
    FROM_DATE_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/input')
    TO_DATE_INPUT   = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input')

    # ===== INIT =====
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # ===== COMMON ACTIONS =====
    def click(self, locator):
        el = WaitUtils.wait_for_clickable(self.wait, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        el.click()

    def type(self, locator, text):
        el = WaitUtils.wait_for_visibility(self.wait, locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
        el.clear()
        for ch in text:
            el.send_keys(ch)

    # Keyboard-safe dropdown selection
    def select_dropdown_option_keyboard(self):
        WaitUtils.wait_for_visibility(
            self.wait,
            (By.XPATH, "//div[@role='listbox']//span")
        )
        active_element = self.driver.switch_to.active_element
        active_element.send_keys(Keys.ARROW_DOWN)
        active_element.send_keys(Keys.ENTER)

    # ===== AUTOCOMPLETE FIXES =====
    def select_employee_from_hint(self):
        input_box = WaitUtils.wait_for_visibility(self.wait, self.EMPLOYEE_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_box)
        WaitUtils.wait_for_visibility(
            self.wait,
            (By.XPATH, "//div[@role='listbox']//span")
        )
        input_box.send_keys(Keys.ARROW_DOWN)
        input_box.send_keys(Keys.ENTER)

    def select_leave_type(self):
        dropdown = WaitUtils.wait_for_clickable(self.wait, self.LEAVE_TYPE_DROPDOWN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        dropdown.click()
        self.select_dropdown_option_keyboard()

    # ===== NAVIGATION =====
    def open_leave_module(self):
        self.click(self.LEAVE_TAB)

    # ===== HELPER: WAIT & FILL DATES VIA JS =====
    def fill_assign_dates(self, from_date, to_date):
        from_input = WaitUtils.wait_for_clickable(self.wait, self.FROM_DATE_INPUT)
        to_input = WaitUtils.wait_for_clickable(self.wait, self.TO_DATE_INPUT)

        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", from_input)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", to_input)

        # Set values via JS (React-safe)
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            from_input, from_date
        )
        self.driver.execute_script(
            "arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('input'));",
            to_input, to_date
        )

    # ===== ADD ENTITLEMENT =====
    def add_entitlement(self, employee_name, leave_type, days):
        self.open_leave_module()
        self.click(self.ENTITLEMENTS_MENU)
        self.click(self.EMPLOYEE_ENTITLEMENTS)

        # Employee field
        self.type(self.EMPLOYEE_INPUT, employee_name)
        self.select_employee_from_hint()
        self.click(self.SEARCH_BTN)
        self.click(self.ADD_BTN)

        # Fill entitlement form
        self.type(self.EMPLOYEE_INPUT, employee_name)
        self.select_employee_from_hint()

        # Leave type dropdown
        self.select_leave_type()

        # Entitlement days
        self.type(self.ENTITLEMENT_DAYS_INPUT, str(days))
        self.click(self.SUBMIT_BTN)
        self.click(self.CONFIRM_BTN)

    # ===== ASSIGN LEAVE =====
    def assign_leave(self, employee_name, leave_type, from_date, to_date, comment=None):
        self.open_leave_module()
        self.click(self.ASSIGN_LEAVE_MENU)

        # Employee field
        self.type(self.EMPLOYEE_INPUT, employee_name)
        self.select_employee_from_hint()

        # Leave type dropdown
        self.select_leave_type()

        # Dates via JS (React-safe)
        self.fill_assign_dates(from_date, to_date)

        # Only type comment if visible
        if comment:
            try:
                comment_box = WaitUtils.wait_for_visibility(self.wait, self.COMMENT_BOX, timeout=3)
                self.type(self.COMMENT_BOX, comment)
            except:
                # Comment box not required for this leave type
                pass

        # Click Submit/Assign button
        self.click(self.SUBMIT_BTN)
