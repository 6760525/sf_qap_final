import os
from pages.base import WebPage
from pages.elements import WebElement


class Pages(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/category/detskie-tovary-7000/'

            super().__init__(web_driver, url)

    main_logo = WebElement(xpath='//*[@id="stickyHeader"]/div[1]/a[1]/img[1]')  # логотип в шапке слева
    toys = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]') #кнопка игрушки и игры
    hygiene = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/a[1]') #кнопка Подгузники и гигиена
    food = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/a[1]') #нопка Детское питание
    prams = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/a[1]') #кнопка Коляски и автокресла
    room = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/a[1]') #кнопка Детская комната
    for_moms = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]/a[1]') #кнопка Товары для мам
    sport = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[7]/a[1]') #кнопка спорт и игры на улице
    best_price_zone = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[8]/a[1]') #кнопка Зона лучших цен!
