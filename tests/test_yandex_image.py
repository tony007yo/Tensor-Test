from pages.image import YandexImagePage

def test_menu_button_exist(browser):
  search_page = YandexImagePage(browser)
  search_page.load_site()
  
  menu_button = search_page.find_menu_button()
  assert menu_button.text == "Все"


def test_link_adress(browser):
  search_page = YandexImagePage(browser)
  search_page.load_site()
  
  search_page.press_image_button()
  assert browser.current_url != "https://yandex.ru/images/"


def test_category_name(browser):
  search_page = YandexImagePage(browser)
  search_page.load_site()
  
  category_names = search_page.check_first_category()

  assert category_names[0] == category_names[1]

def test_image_changing(browser):
  search_page = YandexImagePage(browser)
  search_page.load_site()

  first_image = search_page.open_first_image()

  next_image = search_page.open_next_image()
  assert first_image != next_image

  prev_image = search_page.open_prev_image()
  assert first_image == prev_image
