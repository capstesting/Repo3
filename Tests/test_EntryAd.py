import sys

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass


class TestEntryAd(BaseClass):
    def test_entry_ad(self):
        try:
            self.log=self.getLogger()
            self.entry_Ad=HomePage(self.driver)
            self.entry_Ad.home("Entry Ad",10)
            self.driver.implicitly_wait(10)
            self.log.info(self.driver.find_element_by_xpath('//div[@class="example"]/h3').text)
            self.popup_text=self.driver.find_element_by_xpath('//div[@class="modal-body"]/p').text
            assert "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker)." in self.popup_text
            self.driver.find_element_by_xpath('//div[@class="modal-footer"]/p').click()
            self.driver.info("The pop up is closed.")
            self.log.info(self.driver.find_element_by_xpath('//div[@class="example"]/h3').text)


        except:
            self.log.error(sys.exc_info())
