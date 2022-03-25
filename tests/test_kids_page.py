from pages.kids_page import Pages

def test_mainlogo(web_browser):
    """32.Тестируем нажатие на логотип в шапке сайиа. Ожидаем переход на главнуюстраницу"""
    page = Pages(web_browser)
    page.main_logo.click()

    assert page.get_current_url() == 'https://www.ozon.ru'

def test_toys(web_browser):
    """33.Тестируем кнопку "Игрушки и игры". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.toys.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/igrushki-i-igry-7108/'

def test_hygiene(web_browser):
    """34.Тестируем кнопку "Подгузники и гигиена". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.hygiene.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/podguzniki-i-gigiena-7058/'

def test_food(web_browser):
    """35.Тестируем кнопку "Детское питание". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.food.click()

    assert page.get_current_url() == 'https://www.ozon.ru/highlight/detskoe-pitanie-i-tovary-dlya-kormleniya-219397/'

def test_prams(web_browser):
    """36.Тестируем кнопку "Коляски и автокресла". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.prams.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/kolyaski-i-avtokresla-30482/'

def test_room(web_browser):
    """37.Тестируем кнопку "Детская комната". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.room.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/detskaya-komnata-7041/'

def test_for_moms(web_browser):
    """38.Тестируем кнопку "Товары для мам". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.for_moms.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/tovary-dlya-mam-7077/'

def test_sport(web_browser):
    """39.Тестируем кнопку "Спорт и игры на улице". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.sport.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/sport-i-igry-na-ulitse-30726/'


def test_best_price_zone(web_browser):
    """40.Тестируем кнопку "Зона лучших цен!". Ожидаем переход на сооответствующую страницу"""
    page = Pages(web_browser)
    page.best_price_zone.click()

    assert page.get_current_url() == 'https://www.ozon.ru/highlight/zona-luchshih-tsen-273550/'
