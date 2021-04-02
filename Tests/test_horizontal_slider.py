from time import sleep

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys

import sys

class TestHorizontalSlider(BaseClass):
    def test_horizontal_slider(self):
        try:
            self.log=self.getLogger()
            self.slide=HomePage(self.driver)
            self.slide.home("Horizontal Slider",10)
            self.driver.find_element_by_xpath('//input[@type="range"]').click()
            sleep(4)
            self.originalval=self.driver.find_element_by_xpath('//span[@id="range"]').text
            self.driver.find_element_by_xpath('//input[@type="range"]').send_keys(Keys.ARROW_RIGHT)
            self.changedval=self.driver.find_element_by_xpath('//span[@id="range"]').text
            if float(self.changedval) == float(self.originalval) + 0.5:
                self.log.info("Working fine")
            else:
                self.log.warning("Not working")

        except:
            self.log.error(sys.exc_info())
            assert False