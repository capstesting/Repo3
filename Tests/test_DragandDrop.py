import sys

from selenium.webdriver import ActionChains

from utilities.BaseClass import BaseClass
from PageObjects.home import HomePage


class TestDRAGDROP(BaseClass):
    def test_dragdAndDrop(self):
        try:
            self.log = self.getLogger()
            self.dragdrop = HomePage(self.driver)
            self.dragdrop.home('Drag and Drop', 5)
            self.div1 = self.driver.find_element_by_xpath('//div[@id="column-a"]')
            self.div2 = self.driver.find_element_by_xpath('//div[@id="column-b"]')
            self.action = ActionChains(self.driver)
            self.action.drag_and_drop(self.div2, self.div1).perform()
            self.log.info("Drag and Drop completed!")

        except:
            self.log.error(sys.exc_info())
