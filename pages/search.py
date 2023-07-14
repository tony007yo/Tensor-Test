from .base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class YandexLocators:
  YANDEX_SEARCH_FIELD = (By.ID, "text")
  YANDEX_SUGGESTION = (By.CSS_SELECTOR, "li[class*='mini-suggest__item_type_fulltext']")
  YANDEX_SEARCH_RESULT = (By.ID, "search-result")
  YANDEX_SEARCH_ITEM = (By.XPATH, "//*[@id='search-result']/li[1]/div")
  
class YandexSearchPage(BasePage):
  base_url = 'https://ya.ru/'

  def __init__(self, browser):
    self.browser = browser
  
  @property
  def search_field(self):
    return self.find_element(YandexLocators.YANDEX_SEARCH_FIELD)
  
  @property
  def suggestion(self):
    return self.find_element(YandexLocators.YANDEX_SUGGESTION)

  @property
  def search_result(self):
    return self.find_element(YandexLocators.YANDEX_SEARCH_RESULT)

  @property
  def item(self):
    return self.find_element(YandexLocators.YANDEX_SEARCH_ITEM)


  def find_suggestion(self, phrase):
    search_input = self.search_field
    search_input.clear()
    
    search_input.send_keys(phrase)
    
    return self.suggestion.get_attribute('data-text')
  
  def find_search_result(self, phrase):
    search_input = self.search_field
    search_input.clear()
    
    search_input.send_keys(phrase + Keys.RETURN)
    return self.search_result.text
  
  def get_search_result(self, phrase):
    search_input = self.search_field
    search_input.clear()
    
    search_input.send_keys(phrase + Keys.RETURN)
    return self.item.text.split()