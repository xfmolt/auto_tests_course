#Принять алерт, скопировать текст

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyperclip as pc

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #открываем сайт
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    #Принять конфирм
    confirm = browser.switch_to.alert
    confirm.accept()

    #Считать значение для переменной x. Посчитать математическую функцию от x (код для этого приведён ниже).
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #Ввести ответ в поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    #Скопировать содержимое алерта и закрыть
    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')[-1]
    pc.copy(alert_text)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

