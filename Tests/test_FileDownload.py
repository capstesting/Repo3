from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

class TestFileDownload(BaseClass):
    def test_file_download(self):
        try:
            self.log=self.getLogger()
            self.secure=HomePage(self.driver)
            self.secure.home("Secure File Download",5)
            self.log.info("Page opened successfully")

            self.alert_obj = self.driver.switch_to.alert
            self.alert_obj.send_keys("admin")
            self.alert_obj.send_keys("admin")
            self.alert_obj.accept()

        except:
            self.log.error(sys.exc_info())
            assert False