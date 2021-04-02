import sys

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from PageObjects.home import HomePage


class TestDynamicContent(BaseClass):
    def test_DynamicContent(self):
        try:
            self.log = self.getLogger()
            self.dynamic = HomePage(self.driver)
            self.dynamic.home('Dynamic Content', 5)
            self.row = (By.XPATH, '//div[@class="large-10 columns"]')

            for i in range(2):
                self.rowSelect = self.driver.find_elements(*self.row)
                self.log.warning(self.rowSelect)
                self.j = 0
                for j in range(3):
                    self.rowContent = self.rowSelect[j].text
                    self.log.info(self.rowContent)

                self.driver.refresh()

        except:
            self.log.error(sys.exc_info())
