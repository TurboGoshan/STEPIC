from selenium.webdriver.chrome.webdriver import WebDriver
import time

browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')

try:
    browser.get("http://suninjuly.github.io/registration1.html")
    input1 = browser.find_element_by_xpath('//div[1]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//div[1]/div[2]/input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//div[1]/div[3]/input')
    input3.send_keys("test@qa.com")
    input4 = browser.find_element_by_xpath('//div[2]/div[1]/input')
    input4.send_keys("123456789")
    input5 = browser.find_element_by_xpath('//div[2]/div[2]/input')
    input5.send_keys("Test")
    button = browser.find_element_by_css_selector("button.btn").click()
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()