from selenium.webdriver.chrome.webdriver import WebDriver
import time
import math

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    box = browser.find_element_by_id('treasure')
    box2 = box.get_attribute('valuex')
    x = calc(box2)
    input = browser.find_element_by_id("answer")
    input.send_keys(x)
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()