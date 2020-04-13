import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class edit_post(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/kaitlynbaysa/Desktop/ISQA3900/assign1/chromedriver')

    def test_edit_post(self):
        user = "instructor"
        pwd = "Maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(3)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/")
        assert "Logged In"
        time.sleep(5)

        title = "This is a test post with selenium"
        text = "This is a test post of text with selenium"

        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/h2/a").click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a").click()
        time.sleep(3)
        elem = driver.find_element_by_id(("id_title"))
        elem.clear()
        elem.send_keys(title)
        elem = driver.find_element_by_id(("id_text"))
        elem.clear()
        elem.send_keys(text)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(3)
        driver.get("http://127.0.0.1:8000/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
