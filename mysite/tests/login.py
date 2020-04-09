import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
        driver.get("http://127.0.0.1:8000/admin")
        assert "Logged In"


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
