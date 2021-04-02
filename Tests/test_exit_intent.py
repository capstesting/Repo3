import sys

from selenium.webdriver import ActionChains

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass

'''Not Working'''
class TestExitIntent(BaseClass):
    def test_exit_intent(self):
        try:
            self.log=self.getLogger()
            self.exit=HomePage(self.driver)
            self.exit.home("Exit Intent",10)
            self.action=ActionChains(self.driver)
            self.log.info("Created action object")

            self.log.info("Created model object")
            self.log.info("CHeck done")
            self.action.move_by_offset(0,0).perform()
            self.log.info("Mouse moved by offset")
            self.model = self.driver.find_element_by_xpath('//div[@class="model-body"]')
            if self.model.is_displayed():
                self.log.info("The pop up is displayed")
            else:
                self.log.error("The Pop up is not displayed")
        except:
            self.log.error(sys.exc_info())
            assert False
