import sys
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class TestContextMenu(BaseClass):
    def test_ContextMenu(self):
        try:
            self.log = self.getLogger()
            self.contextmenulink = (By.XPATH, '//a[text()="Context Menu"]')
            self.driver.find_element(*self.contextmenulink).click()
            sleep(5)
            self.reqBox = (By.XPATH, '//div[@id="hot-spot"]')
            self.alertBox = self.driver.find_element(*self.reqBox)
            self.action = ActionChains(self.driver)
            self.action.context_click(self.alertBox).perform()
            self.obj = self.driver.switch_to.alert
            self.alertText = self.obj.text

            if "You selected a context menu" in self.alertText:
                self.log.info("The Alert is working fine")
            else:
                self.log.warning("The text is not present in the alert")

            self.obj.accept()
            self.log.info("The alert is closed.")


        except:
            self.log.error(sys.exc_info())

    # CHanges made for github branches
    def test_ContextMenuGitHub(self):
        try:
            self.log = self.getLogger()
            self.contextmenulink = (By.XPATH, '//a[text()="Context Menu"]')
            self.driver.find_element(*self.contextmenulink).click()
            sleep(5)
            self.reqBox = (By.XPATH, '//div[@id="hot-spot"]')
            self.alertBox = self.driver.find_element(*self.reqBox)
            self.action = ActionChains(self.driver)
            self.action.context_click(self.alertBox).perform()
            self.obj = self.driver.switch_to.alert
            self.alertText = self.obj.text

            if "You selected a context menu" in self.alertText:
                self.log.info("The Alert is working fine")
            else:
                self.log.warning("The text is not present in the alert")

            self.obj.accept()
            self.log.info("The alert is closed.")


        except:
            self.log.error(sys.exc_info())
