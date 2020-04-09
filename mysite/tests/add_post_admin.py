import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/Users/kaitlynbaysa/Desktop/ISQA3900/assign1/chromedriver')

    def test_add_post_admin(self):
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
        time.sleep(3)

        assert "Logged In"

        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)

        driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(1)

        driver.find_element_by_id("id_author").click()
        select = Select(driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[1]/div/div/"
                                                     "select"))
        select.select_by_visible_text("instructor")
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is a test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is a test post of text with selenium")
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[1]/a[1]").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/fieldset/div[5]/div/p/span[2]/a[1]").click()
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()