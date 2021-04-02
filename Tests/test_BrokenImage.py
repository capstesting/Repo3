import sys
from time import sleep
import urllib3
import requests
from selenium.webdriver.common.by import By
from urllib3 import response

from utilities.BaseClass import BaseClass

# This is the Broken Image Test
# Now thi sis the change made by X

class TestBrokenImage(BaseClass):
    def test_BrokenImg(self):
        self.log = self.getLogger()
        try:
            self.requiredlink = (By.XPATH, '//*[@id="content"]/ul/li[4]/a')
            self.log.info("Broken Image link found.")
            self.driver.find_element(*self.requiredlink).click()
            sleep(5)
            self.image_list = self.driver.find_elements_by_tag_name("img")
            self.log.info("Links of image found.")
            for img in self.image_list:
                self.response = requests.get(img.get_attribute('src'), stream=True)
                if self.response.status_code != 200:
                    self.log.warning(img.get_attribute('outerHTML') + " is broken.")
                else:
                    self.log.info(img.get_attribute('outerHTML') + " is working fine.")

        except:
            self.log.error(sys.exc_info())
