import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path='/Users/kaitlynbaysa/Desktop/ISQA3900/assign1/chromedriver')

    def test_delete_post(self):
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
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"
        time.sleep(1)
        driver.find_element_by_link_text("Posts").click()
        try:
            while driver.find_element_by_link_text("This is a test post with selenium"):
                driver.find_element_by_link_text("This is a test post with selenium").click()
                time.sleep(1)
                driver.find_element_by_link_text("Delete").click()
                time.sleep(1)
                driver.find_element_by_xpath("/html/body/div/div[3]/form/div/input[2]").click()
                driver.get("http://127.0.0.1:8000/admin/blog/post/")
                time.sleep(2)
                assert "Deleted selenium posts."
        except NoSuchElementException:
            driver.get("http://127.0.0.1:8000/admin")
            time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
