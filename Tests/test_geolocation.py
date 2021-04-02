from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

'''Working fine'''
class TestGeolocation(BaseClass):
    def test_geolocation(self):
        try:
            self.log = self.getLogger()
            self.geo = HomePage(self.driver)
            self.geo.home("Geolocation", 10)
            self.driver.find_element_by_xpath('//button[text()="Where am I?"]').click()
            self.log.info("Clicked the 'Where am I?' button")
            self.driver.implicitly_wait(5)
            self.lat = self.driver.find_element_by_xpath('//div[@id="lat-value"]').text
            self.long = self.driver.find_element_by_xpath('//div[@id="long-value"]').text
            self.log.info("Latitude: " + self.lat)
            self.log.info("Longitude: " + self.long)
            self.driver.close()

        except:
            self.log.error(sys.exc_info())
            assert False
