from selenium.webdriver.chrome.webdriver import WebDriver
import time
import math

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    button1 = browser.find_element_by_css_selector('[type="submit"]').click()
    alert = browser.switch_to.alert
    alert.accept()
    value = browser.find_element_by_id('input_value')
    x = int(value.text)
    sum = (math.log(abs(12*math.sin(x))))
    input2 = browser.find_element_by_id('answer')
    input2.send_keys(str(sum))
    button2 = browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(3)
    browser.quit()