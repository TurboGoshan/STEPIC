from selenium.webdriver.chrome.webdriver import WebDriver
import time
import math

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button1 = browser.find_element_by_css_selector('button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    value = browser.find_element_by_id('input_value')
    x = value.text
    sum = str(math.log(abs(12 * math.sin(int(x)))))
    input = browser.find_element_by_id('answer')
    input.send_keys(sum)
    time.sleep(1)
    button2 = browser.find_element_by_css_selector('button.btn').click()


finally:
    time.sleep(2)
    browser.quit()