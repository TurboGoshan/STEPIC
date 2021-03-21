from selenium.webdriver.chrome.webdriver import WebDriver
import time

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get('http://suninjuly.github.io/huge_form.html')
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("QA")

    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(4)
    browser.quit()