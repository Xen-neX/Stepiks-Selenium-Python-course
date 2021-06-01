import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price",), '$100')
    )
    print(price)

    button.click()

    input1 = browser.find_element_by_id("input_value")
    input1 = input1.text

    input1_1 = browser.find_element_by_id("answer")
    input1_1.send_keys(calc(input1))

    button1 = browser.find_element_by_id("solve")
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
