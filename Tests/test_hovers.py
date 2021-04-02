from time import sleep

from selenium.webdriver import ActionChains
from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

class TestHovers(BaseClass):
    def test_hovers(self):
        try:
            self.log=self.getLogger()
            self.hovers=HomePage(self.driver)
            self.action=ActionChains(self.driver)
            self.hovers.home("Hovers",10)
            self.img1=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/img')
            self.img2=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/img')
            self.img3=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/img')

            self.action.move_to_element(self.img1).perform()
            self.log.info(self.img1.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/h5').text)

            self.action.move_to_element(self.img2).perform()
            self.log.info(self.img2.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/h5').text)

            self.action.move_to_element(self.img3).perform()
            self.log.info(self.img3.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/h5').text)

        except:
            self.log.error(sys.exc_info())
            assert False
