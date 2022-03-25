#содержит классы для основной страницы

import os
from pages.base import WebPage
from pages.elements import WebElement
from selenium.webdriver.common.by import By


class Pages(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/'
            #главная страница ozon.ru

        super().__init__(web_driver, url)

    field_search = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div[1]/form[1]/div[2]/input[1]') #строка поиска
    button_search = WebElement(xpath='//*[@id="stickyHeader"]/div[3]/div[1]/form[1]/button[1]') #кнопка поиска
    message_search = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]') #результат поиска
    catalog = WebElement(xpath='//*[@id="stickyHeader"]/div[2]/div[1]/div[1]/button[1]/span[1]') #кнопка КАТАЛОГ
    topfashion = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[1]/a[1]') #кнопка Top Fashion
    premium = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[2]/a[1]') #кнопка Premium
    ozontravel = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[3]/a[1]') #кнопка OzonTravel
    ozonexpress = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[4]/a[1]') #кнопка OzonExpress
    ozonschet = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[5]/a[1]') #Кнопка Ozon Счёт
    live = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[6]') #кнопка LIVE
    actions = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[7]/a[1]') #кнопка Акции
    brends = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[8]/a[1]') #кнопка Бренды
    shops = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[9]/a[1]') #кнопка Магазины
    elektronika = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[10]/a[1]') #кнопка Электроника
    clothers = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[11]/a[1]') #кнопка Одежда и обувь
    childgoods = WebElement(xpath='//*[@id="layoutPage"]/div[1]/header[1]/div[2]/div[1]/ul[1]/li[12]/a[1]') #кнопка Детские товары
    mine = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/div[1]/div[1]/a[1]') #кнопка входа в личный кабинет
    orders = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/div[2]/a[1]') #кнопка Заказы
    favorites = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/a[1]') #кнопка Любимые товары
    cart = WebElement(xpath='//*[@id="stickyHeader"]/div[4]/a[2]') #кнопка Корзина
    city = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]') #кнопка выбора города в левом верхнем углу
    field_city = WebElement(xpath='body/div[20]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/label[1]/div[1]/div[1]/input[1]') #поле поиска города
    click_city = WebElement(xpath='body/div[20]/div[1]/div[2]/div[1]/div[1]/div[2]/ul[1]/li[1]/a[1]') #выбор первого города из списка
    message_city = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[1]/div[1]/div[1]/button[1]/span[1]/span[1]') #название выбранного города
    smartphone = WebElement(xpath='//*[@id="stickyHeader"]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]') #раздел Смартфоны из каталога
    sort_list = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]') #список вариантов сортировки товаров
    cheap_first = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]') #сортировка сначала дешёвые
    buy = WebElement(xpath='//*[@id="layoutPage"]/div[1]/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/button[1]/span[1]') #добавить в корзину первый товар из списка
    delete_in_cart = WebElement(xpath='//*[@id="split-Main-0"]/div[2]/div[2]/div[2]/span[2]') #кнопка удаления товара из корзины
    delete_goods = WebElement(xpath='body/div[11]/div[1]/div[2]/div[1]/div[1]/section[1]/div[3]/div[1]/button[1]/span[1]') #подтверждение удаления товара
    link_VK = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer[1]/div[1]/div[1]/div[5]/div[2]/a[1]/svg[1]') #иконка для перехода в группу VK
    link_facebook = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer[1]/div[1]/div[1]/div[5]/div[2]/a[2]/svg[1]') #иконка для перехода на страницу Facebook
    link_twitter = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer[1]/div[1]/div[1]/div[5]/div[2]/a[3]/svg[1]') #иконка для перехода на страницу Twitter
    link_instagram = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer[1]/div[1]/div[1]/div[5]/div[2]/a[4]/svg[1]') #иконка для перехода на страницу Instagram
    link_telegram = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer[1]/div[1]/div[1]/div[5]/div[2]/a[5]/svg[1]') #иконка для перехода в Telegram
    button_visually_impaired = WebElement(xpath='//*[@id="layoutPage"]/div[1]/footer[1]/div[1]/div[1]/div[5]/div[3]/div[1]/button[1]/span[1]') #кнопка версия для слабовидящих

