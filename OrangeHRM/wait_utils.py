from selenium.webdriver.support import expected_conditions as EC




class WaitUtils:


   @staticmethod
   def wait_for_visibility(wait, locator, timeout=None):
       if timeout:
           return wait.until(EC.visibility_of_element_located(locator), timeout)
       return wait.until(EC.visibility_of_element_located(locator))


   @staticmethod
   def wait_for_clickable(wait, locator, timeout=None):
       if timeout:
           return wait.until(EC.element_to_be_clickable(locator), timeout)
       return wait.until(EC.element_to_be_clickable(locator))


   @staticmethod
   def wait_for_invisibility(wait, locator, timeout=None):
       if timeout:
           return wait.until(EC.invisibility_of_element_located(locator), timeout)
       return wait.until(EC.invisibility_of_element_located(locator))
