from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys


class TestInputs(BaseClass):
    def test_inputs(self):
        try:
            self.log=self.getLogger()
            self.inputs=HomePage(self.driver)
            self.inputs.home("Inputs",5)
            self.driver.find_element_by_xpath('//input[@type="number"]').click()
            self.action = ActionChains(self.driver)

            self.action.send_keys(Keys.UP).perform()
            self.original = self.driver.find_element_by_xpath('//input[@type="number"]').text

            sleep(2)

            self.action.send_keys(Keys.UP).perform()
            self.final = self.driver.find_element_by_xpath('//input[@type="number"]').text

            sleep(2)

            self.log.info("Working fine")


        except:
            self.log.error(sys.exc_info())
            assert False