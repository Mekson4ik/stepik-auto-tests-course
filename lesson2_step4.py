from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname').send_keys('Max')
    input2 = browser.find_element_by_name('lastname').send_keys('Max')
    input3 = browser.find_element_by_name('email').send_keys('Max')
    file_path = os.path.join(os.path.dirname(__file__), 'file.txt')
    file = browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
