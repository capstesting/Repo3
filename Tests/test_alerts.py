from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
from time import sleep
import sys


class TestAlerts(BaseClass):
    def test_alerts(self):
        try:
            self.log = self.getLogger()
            self.alert = HomePage(self.driver)
            self.alert.home("JavaScript Alerts", 5)

            self.log.info("First Button")
            self.driver.find_element_by_xpath('//button[text()="Click for JS Alert"]').click()

            self.alert_obj = self.driver.switch_to.alert
            self.log.info("Alert box text is: " + self.alert_obj.text)
            sleep(2)
            self.alert_obj.accept()
            self.log.info("Here")
            sleep(2)

            if "You successfully clicked an alert" in self.driver.find_element_by_xpath('//p[@id="result"]').text:
                self.log.info("First alert working fine.")
            else:
                self.log.critical("First alert not working")

            self.log.info("Second Button")
            self.driver.find_element_by_xpath('//button[text()="Click for JS Confirm"]').click()
            self.log.info("Alert box text is: " + self.alert_obj.text)
            self.alert_obj.dismiss()
            if "You clicked: Cancel" in self.driver.find_element_by_xpath('//p[@id="result"]').text:
                self.log.info("Second alert working fine.")
            else:
                self.log.critical("Second alert not working")

            self.log.info("Third Button")
            self.driver.find_element_by_xpath('//button[text()="Click for JS Prompt"]').click()
            self.log.info("Alert box text is: " + self.alert_obj.text)
            self.alert_obj.send_keys("Sample")
            self.alert_obj.accept()
            if "You entered: Sample" in self.driver.find_element_by_xpath('//p[@id="result"]').text:
                self.log.info("Third alert working fine.")
            else:
                self.log.critical("Third alert not working")


        except:
            self.log.error(sys.exc_info())
            assert False
