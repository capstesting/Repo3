from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

class TestKeyPresses(BaseClass):
    def test_key_presses(self):
        try:
            self.log=self.getLogger()
            self.key=HomePage(self.driver)
            self.key.home("Key Presses",5)
            self.log.info("Page opened successfully")

            self.action=ActionChains(self.driver)
            self.action.send_keys(Keys.UP).perform()
            if "You entered: UP" in self.driver.find_element_by_xpath('//p[@id="result"]').text:
                self.log.info("UP Key detected successfully")
            else:
                self.log.critical("Key not detected")
                assert False

            self.action.send_keys(Keys.DOWN).perform()
            if "You entered: DOWN" in self.driver.find_element_by_xpath('//p[@id="result"]').text:
                self.log.info("DOWN Key detected successfully")
            else:
                self.log.critical("Key not detected")
                assert False



        except:
            self.log.error(sys.exc_info())
            assert False