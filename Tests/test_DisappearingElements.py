import sys
from time import sleep

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestDisappearingElements(BaseClass):
    def test_DisappearingElements(self):
        try:
            self.log = self.getLogger()
            self.disappearingElement = (By.XPATH, '//a[text()="Disappearing Elements"]')
            self.driver.find_element(*self.disappearingElement).click()
            sleep(5)
            self.reqButtons = self.driver.find_elements_by_tag_name('a')
            self.reqList = []
            for i in self.reqButtons:
                self.reqList.append(i.text.strip())
            while "Gallery" not in self.reqList:
                self.reqButtons = self.driver.find_elements_by_tag_name('a')
                self.reqList = []
                for i in self.reqButtons:
                    self.reqList.append(i.text.strip())
                self.log.info("Current buttons are: " + ' '.join(self.reqList))
                self.driver.refresh()
                sleep(3)

            self.log.info("Gallery button found")

        except:
            self.log.error(sys.exc_info())
