from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
  base_url = ""
  wait_time = 20

  def __init__(self, browser):
    self.browser = browser
    
  def find_element(self, locator, time = wait_time, err_msg = ""):
    if not err_msg:
      err_msg = "Failed because of captcha" if "showcaptcha" in self.browser.current_url \
        else f"Can't find element by locator {locator}"
      
    return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                    message=f"{err_msg}")

  def find_elements(self, locator, time = wait_time, err_msg = ""):
    if not err_msg:
      err_msg = "Failed because of captcha" if "showcaptcha" in self.browser.current_url \
        else f"Can't find elements by locator {locator}"
      
    return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                    message=f"{err_msg}")

  def load_site(self):
    return self.browser.get(self.base_url)