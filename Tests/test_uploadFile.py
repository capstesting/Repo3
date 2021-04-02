from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys
from time import sleep

'''Working Fine'''
class TestUploadFile(BaseClass):
    def test_upload_file(self):
        try:
            self.log=self.getLogger()
            self.upload=HomePage(self.driver)
            self.upload.home("File Upload",10)
            self.log.info("FIle upload page opened")
            self.driver.implicitly_wait(10)
            self.loc="C:\\Users\\Anmol\\Downloads\\Sample.pdf"
            self.log.info("Location successfully picked")
            self.choose=self.driver.find_element_by_xpath('//input[@id="file-upload"]')
            self.log.info("The Choose File button selected")
            self.choose.send_keys(self.loc)
            self.log.info("Value sent to the button")
            sleep(5)
            self.driver.find_element_by_xpath('//input[@id="file-submit"]').click()
            self.log.info("Clicked on Upload button")
            self.driver.implicitly_wait(5)
            if "File Uploaded!" in self.driver.find_element_by_xpath('//h3').text:
                self.log.info("File uploaded successfully")
            else:
                self.log.error("File not uploaded successfully")

        except:
            self.log.error(sys.exc_info())
            assert False