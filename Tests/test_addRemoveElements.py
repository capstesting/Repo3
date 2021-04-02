import sys
from time import sleep
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestAddRemoveElements(BaseClass):
    def test_AddRemoveButtons(self):
        self.log = self.getLogger()
        try:
            self.driver.find_element_by_xpath('//a[text()="Add/Remove Elements"]').click()
            sleep(5)
            self.add = (By.XPATH, '//button[text()="Add Element"]')
            self.delete = (By.XPATH, '//button[text()="Delete"]')
            self.countDelete = 0
            self.deleteNumber = self.driver.find_elements(*self.delete)
            for i in range(1, 50):
                self.driver.find_element(*self.add).click()
                self.log.info("Clicked on Add Element. Current count= " + str(i))
                self.tempDel = len(self.deleteNumber)
                self.countDelete += 1
                self.log.info("Count for Expected Delete increased to " + str(self.countDelete))
                if self.tempDel == self.countDelete:
                    self.log.info("Number of Delete buttons is as Expected")

        except:
            self.log.error(sys.exc_info())
