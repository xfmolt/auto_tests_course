#Ждем нужный текст на странице. Бронируем дом по СТРОГО заданной цене. Решаем уравнение и скроллим

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip as pc
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    #Найти нашу кнопку и нажать
    button = browser.find_element(By.ID, "book")
    button.click()

    #Проскроллить до следующей кнопки
    submit_button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    # Считать значение для переменной x. Посчитать математическую функцию от x (код для этого приведён ниже).
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #Ввести ответ в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    submit_button.click()

     # Скопировать содержимое алерта и закрыть
    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')[-1]
    pc.copy(alert_text)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

