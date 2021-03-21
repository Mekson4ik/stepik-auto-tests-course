from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # функция calc(), которая рассчитает и вернет значение функции, которое нужно ввести в текстовое поле
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    input1 = browser.find_element_by_id('answer').send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    option1 = browser.find_element_by_css_selector("[type='checkbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()

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
