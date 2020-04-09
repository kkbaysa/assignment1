import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def delete_post(driver):
    driver.get("http://127.0.0.1:8000/admin")
    elem = driver.find_element_by_link_text("Posts").click()
    try:
        while driver.find_element_by_link_text("This is a test post with selenium"):
            driver.find_element_by_link_text("This is a test post with selenium").click()
            elem = driver.find_element_by_link_text("Delete").click()
            driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
            driver.get("http://127.0.0.1:8000/admin/blog/post/")
            assert "Deleted selenium posts."
    except NoSuchElementException:
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(2)


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/kaitlynbaysa/Desktop/ISQA3900/assign1/chromedriver')

    def test_login(self):
        user = "instructor"
        pwd = "Maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        assert "Logged In"
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(5)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a test post of text with selenium")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        assert "Posted Blog Entry"
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)
        delete_post(driver)

    def tearDown(self):
        self.driver.quit()




if __name__ == "__main__":
    unittest.main()
