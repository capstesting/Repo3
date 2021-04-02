import sys

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass

'''Working Fine'''
class TestDownload(BaseClass):
    def test_download(self):
        try:
            self.log=self.getLogger()
            self.down=HomePage(self.driver)
            self.down.home("File Download",10)
            self.driver.find_element_by_xpath('//a[text()="some-file.txt"]').click()
            self.log.info("First file downloaded")
        except:
            self.log.error(sys.exc_info())
            assert False