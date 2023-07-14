import pytest
import logging

from selenium.webdriver import Chrome

@pytest.fixture(scope="session")
def browser():
  driver = Chrome()
  driver.implicitly_wait(20)
  driver.maximize_window()
  try:
    yield driver
  except Exception as ex:
    logging.error(ex)
  finally:
    driver.quit()
