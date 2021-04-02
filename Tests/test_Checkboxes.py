import sys
from time import sleep

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestCheckox(BaseClass):
    def test_checkBox(self):
        self.log = self.getLogger()
        try:
            self.reqlink = (By.XPATH, '//a[text()="Checkboxes"]')
            self.driver.find_element(*self.reqlink).click()
            sleep(5)
            self.check1 = (By.XPATH, '//*[@id="checkboxes"]/input[1]')
            self.check2 = (By.XPATH, '//*[@id="checkboxes"]/input[2]')

            self.driver.find_element(*self.check1).click()
            self.log.info("Checkbox 1 is checked")

            self.driver.find_element(*self.check2).click()
            self.log.info("Checkbox 2 is unchecked")

        except:
            self.log.error(sys.exc_info())
