from selenium.webdriver.chrome.webdriver import WebDriver
import time

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/math.html")
    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robot radio: ", robots_checked)
    assert robots_checked != 'true'

finally:
    time.sleep(1)
    browser.quit()