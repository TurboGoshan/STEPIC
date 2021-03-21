from selenium.webdriver.chrome.webdriver import WebDriver
import time
import math

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://SunInJuly.github.io/execute_script.html")
    value = browser.find_element_by_id('input_value')
    x = value.text
    count = str(math.log(abs(12*math.sin(int(x)))))
    footer = browser.find_element_by_css_selector('footer.text-muted')
    browser.execute_script('arguments[0].style.visibility =\'hidden\'', footer)
    input = browser.find_element_by_id('answer')
    input.send_keys(count)
    checkbox = browser.find_element_by_css_selector('[type="checkbox"]').click()
    radio = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(3)
    browser.quit()