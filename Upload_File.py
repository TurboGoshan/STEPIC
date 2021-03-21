from selenium.webdriver.chrome.webdriver import WebDriver
import time
import os

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/file_input.html")
    first = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    first.send_keys('Test')
    last = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    last.send_keys('Test')
    email = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    email.send_keys('email@test.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector('[type="submit"]').click()

finally:
    time.sleep(3)
    browser.quit()