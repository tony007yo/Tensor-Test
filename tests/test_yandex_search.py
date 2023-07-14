from pages.search import YandexSearchPage

PHRASE = 'Тензор'

def test_search(browser):
  search_page = YandexSearchPage(browser)
  search_page.load_site()
  
  suggestion = search_page.find_suggestion(PHRASE)
  assert suggestion != ''


def test_search_correct(browser):
  search_page = YandexSearchPage(browser)
  search_page.load_site()

  search_result = search_page.find_search_result(PHRASE)
  assert search_result != ''


def test_search_result(browser):
  search_page = YandexSearchPage(browser)
  search_page.load_site()

  search_result = search_page.get_search_result(PHRASE)
  assert "tensor.ru" in search_result