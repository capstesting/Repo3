import sys
from time import sleep
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class TestBasicAuth(BaseClass):
    def test_BasicAuth(self):
        self.log = self.getLogger()
        try:
            self.driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a').click()
            sleep(5)
            self.parent_window = self.driver.window_handles[0]
            self.child_window = self.driver.window_handles[1]
            self.switch_to.window(self.child_window)


        except:
            self.log.error(sys.exc_info())
