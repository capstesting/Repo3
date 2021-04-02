import sys
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from PageObjects.home import HomePage


class TestDropDown(BaseClass):
    def test_dropdown(self):
        try:
            self.log = self.getLogger()
            self.dropdown = HomePage(self.driver)
            self.dropdown.home('Dropdown', 5)
            self.dropAttr = (By.XPATH, '//select[@id="dropdown"]/option[text()="Option 1"]')
            self.driver.find_element(*self.dropAttr).click()
            self.log.info("Option selected from the dropdown and hence the case is completed!")

        except:
            self.log.error(sys.exc_info())
