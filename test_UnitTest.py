from selenium.webdriver.chrome.webdriver import WebDriver
import unittest


browser = WebDriver(executable_path='D:\Selenium\chromedriver.exe')


class Test_unit(unittest.TestCase):
    def test_1(self):

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
        self.assertEqual (("Congratulations! You have successfully registered!"), welcome_text, "Text exists")
        browser.quit()

    def test_2(self):
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector('[placeholder="Input your name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input2.send_keys("Test@qa.com")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your phone"]')
        input3.send_keys("123456789")
        input4 = browser.find_element_by_css_selector('[placeholder="Input your address"]')
        input4.send_keys("Test 12")
        button = browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual (("Congratulations! You have successfully registered!"), welcome_text, "Text exists")
        browser.quit()

if __name__ == "__main__":
    unittest.main()