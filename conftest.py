import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def setup_class(request):
   options = Options()
   options.add_argument("--incognito")
   driver = webdriver.Chrome(options=options)
   driver.maximize_window()
   driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
   wait = WebDriverWait(driver, 10)


   # Attach driver and wait to the test class
   request.cls.driver = driver
   request.cls.wait = wait


   yield
   driver.quit()
