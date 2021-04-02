from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

class TestMultipleWidows(BaseClass):
    def test_windows(self):
        try:
            self.log=self.getLogger()
            self.wind=HomePage(self.driver)
            self.wind.home("Multiple Windows",5)
            self.log.info("Opened page successfully")

            self.driver.find_element_by_xpath('//a[text()="Click Here"]').click()

            if len(self.driver.window_handles) ==2:
                self.log.info("New window opened")
            else:
                self.log.error("Window nt opened")
                assert False

            self.driver.switch_to.window(self.driver.window_handles[1])
            if "New Window" in self.driver.find_element_by_xpath('//h3').text:
                self.log.info("Window switched successfully")
            else:
                self.log.critical("Window not switched")
                assert False

            self.driver.switch_to.window(self.driver.window_handles[0])
            if "Opening a new window" in self.driver.find_element_by_xpath('//h3').text:
                self.log.info("Window switched successfully")
            else:
                self.log.critical("Window not switched")
                assert False



        except:
            self.log.error(sys.exc_info())
            assert False