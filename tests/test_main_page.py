from pages.base_page import Pages
import time

def test_search_field_positive(web_browser):
    """1. Тестирование строки поиска. Поиск товара"""
    page = Pages(web_browser)
    page.field_search.send_keys('телевизор')
    page.button_search.click()

    assert page.message_search


def test_search_field_letters(web_browser):
    """2.Тестирование строки поиска. Несуществующий товар."""
    page = Pages(web_browser)
    page.field_search.send_keys('фываолдж')
    page.button_search.click()

    assert page.message_result.get_text() == 'Простите, по вашему запросу товаров сейчас нет.'


def test_search_field_numbers(web_browser):
    """3.Тестирование cтроки поиска. Числовой запрос"""
    page = Pages(web_browser)
    page.field_search.send_keys('1234567890987654321')
    page.button_search.click()

    assert page.message_result.get_text() == 'Мы ничего не нашли по вашему запросу! Что делать?'


def test_catalog(web_browser):
    """4.Тестируем кнопку "Каталог".Ожидаем открытие выпадающего меню. Делаем скриншот и сохраняем в файл"""
    page = Pages(web_browser)
    page.catalog.click()
    time.sleep(2)
    web_browser.save_screenshot('IMG/result1.png')


def test_topfashion(web_browser):
    """5.Тестируем кнопку "TOP Fashion".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.topfashion.click()

    assert page.get_current_url() == 'https://www.ozon.ru/highlight/top-fashion/'


def test_topfashion(web_browser):
    """6.Тестируем кнопку "Premium".Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.topfashion.click()

    assert page.get_current_url() == 'https://www.ozon.ru/highlight/premium/'


def test_ozontravel(web_browser):
    """7. Тестируем кнопку "Ozon Travel". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.ozontravel.click()

    assert page.get_current_url() == 'https://www.ozon.ru/travel/?perehod=ozon_menu_header'


def test_ozonexpress(web_browser):
    """8. Тестируем кнопку "Ozon Express". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.ozonexpress.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/supermarket-25000/?miniapp=supermarket'


def test_ozonschet(web_browser):
    """9. Тестируем кнопку "Ozon Счёт". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.ozonschet.click()

    assert page.get_current_url() == 'https://www.ozon.ru/highlight/keshbek-do-30-dlya-ozon-schet-i-premium-323369/'


def test_live(web_browser):
    """10. Тестируем кнопку "LIVE". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.live.click()

    assert page.get_current_url() == 'https://www.ozon.ru/live/'


def test_actions(web_browser):
    """11. Тестируем кнопку "Акции". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.actions.click()

    assert page.get_current_url() == 'https://www.ozon.ru/info/actions/'


def test_brends(web_browser):
    """12. Тестируем кнопку "Бренды". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.brends.click()

    assert page.get_current_url() == 'https://www.ozon.ru/brand/'


def test_shops(web_browser):
    """13. Тестируем кнопку "Магазины". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.shops.click()

    assert page.get_current_url() == 'https://www.ozon.ru/seller/'


def test_actions(web_browser):
    """14. Тестируем кнопку "Электроника". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.elektronika.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/elektronika-15500/'


def test_clothers(web_browser):
    """15. Тестируем кнопку "Одежда и обувь". Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.clothers.click()

    assert page.get_current_url() == 'https://www.ozon.ru/info/main-apparel/'


def test_childgoods(web_browser):
    """16. Тестируем кнопку "Детские товары". Ожидаем переход на соответствующую страницу """
    page = Pages(web_browser)
    page.childgoods.click()

    assert page.get_current_url() == 'https://www.ozon.ru/category/detskie-tovary-7000/'


def test_mine(web_browser):
    """17. Тестируем кнопку входа в личный кабинет. Ожидаем переход на соответствующую страницу """
    page = Pages(web_browser)
    page.mine.click()

    assert page.get_current_url() == 'https://www.ozon.ru/my/main'


def test_orders(web_browser):
    """18. Тестируем кнопку "Заказы". Ожидаем переход на соответствующую страницу """
    page = Pages(web_browser)
    page.orders.click()

    assert page.get_current_url() == 'https://www.ozon.ru/my/orderlist'


def test_favorites(web_browser):
    """19. Тестируем кнопку "Избранное". Ожидаем переход на соответствующую страницу """
    page = Pages(web_browser)
    page.favorites.click()

    assert page.get_current_url() == 'https://www.ozon.ru/my/favorites'


def test_cart(web_browser):
    """20. Тестируем кнопку "Корзина". Ожидаем переход на соответствующую страницу """
    page = Pages(web_browser)
    page.cart.click()

    assert page.get_current_url() == 'https://www.ozon.ru/cart'


def test_city(web_browser):
    """21. Тестируем кнопку выбора города. Выбор города из списка"""
    page = Pages(web_browser)
    page.city.click()
    page.field_city.send_keys("Саратов")
    page.click_city.click()

    assert page.message_city


def test_sort_cheap_first(web_browser):
    """22. Тестируем сортировку товаров по возрастанию цены. Длеаем скриншот."""
    page = Pages(web_browser)
    page.catalog.click()
    page.smartphone.click()
    page.cheap_first.click()
    time.sleep(2)
    web_browser.save_screenshot('IMG/result2.png')


def test_buy(web_browser):
    """23. Тестируем добавление товара в корзину"""
    page = Pages(web_browser)
    page.field_search.send_keys('валенки женские')
    page.button_search.click()
    page.buy.click()
    time.sleep(10)
    page.cart.click()
    time.sleep(10)
    web_browser.save_screenshot('IMG/result3.png')


def test_delete_from_cart(web_browser):
    """24. Тестируем удаление товара из корзины"""
    page = Pages(web_browser)
    page.cart.click()
    time.sleep(10)
    page.delete_in_cart.click()
    time.sleep(10)
    page.delete_goods.click()
    time.sleep(10)

    web_browser.save_screenshot('IMG/result4.png')


def test_scroll_down(web_browser):
    """25.Тестируем прокрутку по вертикали вниз."""
    page = Pages(web_browser)
    page.scroll_footer()
    time.sleep(5)

    web_browser.save_screenshot('images/result5.png')


def test_vk(web_browser):
    """26. Тестируем кнопку перехода на страницу в VK. Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_VK.click()

    assert page.get_current_url() == 'https://vk.com/ozon'


def test_facebook(web_browser):
    """27. Тестируем кнопку перехода на страницу в Facebook. Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_facebook.click()

    assert page.get_current_url() == 'https://www.facebook.com/ozon.ru'


def test_twitter(web_browser):
    """28. Тестируем кнопку перехода на страницу в Twitter. Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_twitter.click()

    assert page.get_current_url() == 'https://twitter.com/Ozon_ru/'


def test_instagram(web_browser):
    """29. Тестируем кнопку перехода на страницу в Instagram. Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_instagram.click()

    assert page.get_current_url() == 'https://www.instagram.com/ozonru/'


def test_telegram(web_browser):
    """30. Тестируем кнопку перехода на страницу в Telegram. Ожидаем переход на соответствующую страницу"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.link_telegram.click()

    assert page.get_current_url() == 'https://t.me/ozonhq'


def test_visually_impaired(web_browser):
    """31. Тестируем кнопку перехода на режим для слабовидящих. Делаем скриншот"""
    page = Pages(web_browser)
    page.scroll_footer()
    page.button_visually_impaired.click()
    time.sleep(5)

    web_browser.save_screenshot('images/result6.png')
