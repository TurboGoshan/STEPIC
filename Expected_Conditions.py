from selenium.webdriver.chrome.webdriver import WebDriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button1 = browser.find_element_by_id('book')
    book = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    button1.click()
    value = browser.find_element_by_id('input_value')
    x = value.text
    count = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element_by_id('answer')
    input.send_keys(count)
    button2 = browser.find_element_by_id('solve').click()

finally:
    time.sleep(3)
    browser.quit()