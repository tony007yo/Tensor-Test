import sys

from .base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class YandexLocators:
  YANDEX_BASE_SEARCH_FIELD = (By.ID, "text")
  YANDEX_SEARCH_FIELD = (By.CLASS_NAME, "mini-suggest__input")
  YANDEX_SUGGEST_BUTTON = (By.XPATH, "//li[@class='services-suggest__list-item-more']")
  YANDEX_IMAGE_BUTTON = (By.XPATH, "//*[@aria-label='Картинки']")
  YANDEX_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item")
  YANDEX_BODY = (By.TAG_NAME, "body")
  YANDEX_FIRST_IMAGE = (By.CSS_SELECTOR, "div[class*='serp-item_pos_0']")
  YANDEX_OPENED_IMAGE = (By.XPATH, "//img[@class='MMImage-Origin']")
  YANDEX_PREV_IMAGE = (By.CLASS_NAME, "MediaViewer-ButtonPrev")
  YANDEX_NEXT_IMAGE = (By.CLASS_NAME, "MediaViewer-ButtonNext")

class YandexImagePage(BasePage):
  base_url = 'https://ya.ru/'


  def __init__(self, browser):
    self.browser = browser
  
  @property
  def base_search_field(self):
    return self.find_element(YandexLocators.YANDEX_BASE_SEARCH_FIELD)

  @property
  def search_field(self):
    return self.find_element(YandexLocators.YANDEX_SEARCH_FIELD)
  
  @property
  def suggest_button(self):
    return self.find_element(YandexLocators.YANDEX_SUGGEST_BUTTON)

  @property
  def image_button(self):
    return self.find_element(YandexLocators.YANDEX_IMAGE_BUTTON)
  
  @property
  def first_category(self):
    return self.find_element(YandexLocators.YANDEX_FIRST_CATEGORY)
  
  @property
  def body(self):
    return self.find_element(YandexLocators.YANDEX_BODY)
  
  @property
  def first_image(self):
    return self.find_element(YandexLocators.YANDEX_FIRST_IMAGE)
  
  @property
  def opened_image(self):
    return self.find_element(YandexLocators.YANDEX_OPENED_IMAGE, err_msg="The image did not open!")
  
  @property
  def prev_image(self):
    return self.find_element(YandexLocators.YANDEX_PREV_IMAGE)
  
  @property
  def next_image(self):
    return self.find_element(YandexLocators.YANDEX_NEXT_IMAGE)


  def __copy_operation(self):
    cmd_ctrl = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL

    ActionChains(self.browser)\
        .key_down(Keys.SHIFT)\
        .send_keys(Keys.ARROW_LEFT)\
        .send_keys(Keys.ARROW_UP)\
        .key_up(Keys.SHIFT)\
        .key_down(cmd_ctrl)\
        .send_keys("xvv")\
        .perform()  

  def next_tab(self):
    body = self.body
    body.send_keys(Keys.CONTROL + Keys.TAB)

  def press_search(self):
    search_input = self.base_search_field
    search_input.clear()
    
    search_input.click()

  def find_menu_button(self):
    self.press_search()
    
    return self.suggest_button
  
  def press_image_button(self):
    self.press_search()
    
    sugest = self.suggest_button
    sugest.click()

    image = self.image_button
    image.click()
  
  def check_first_category(self):
    self.press_image_button()

    self.browser.close()
    self.browser.switch_to.window(self.browser.window_handles[0])
    
    first_category = self.first_category
    first_category_name = first_category.text
    first_category.click()
    
    search_field = self.search_field
    input_text = search_field.get_attribute('value')
    
    return (input_text, first_category_name)

  def _get_image_url(self):
    return self.opened_image.get_attribute('src')
  
  def open_next_image(self):
    next_image = self.next_image
    next_image.click()

    return self._get_image_url()

  def open_prev_image(self):
    prev_image = self.prev_image
    prev_image.click()

    return self._get_image_url()

  def open_first_image(self):
    self.check_first_category()

    first_image = self.first_image
    first_image.click()

    return self._get_image_url()
