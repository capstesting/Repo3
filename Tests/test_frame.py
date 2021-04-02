from time import sleep

from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

'''Working Fine'''
class TestFrames(BaseClass):
    def test_frames(self):
        try:
            self.log = self.getLogger()
            self.frame = HomePage(self.driver)
            self.frame.home("Frames", 5)
            self.driver.find_element_by_xpath('//a[text()="iFrame"]').click()
            if "An iFrame containing the TinyMCE WYSIWYG Editor" in self.driver.find_element_by_xpath('//h3').text:
                self.log.info("Navigated to the correct page")
            else:
                self.log.error("Wrong Page")
            self.iframe = self.driver.find_element_by_xpath('//iframe[@id="mce_0_ifr"]')
            self.driver.switch_to.frame(self.iframe)
            self.driver.find_element_by_xpath('//*[@id="tinymce"]/p').send_keys("This is the changed frame.ss")
            self.driver.close()
        except:
            self.log.error(sys.exc_info())
            assert False

    def test_nestedframes(self):
        try:
            self.log = self.getLogger()
            self.frame = HomePage(self.driver)
            self.frame.home("Frames", 5)
            self.driver.find_element_by_xpath('//a[text()="Nested Frames"]').click()
            self.topFrame = self.driver.find_element_by_xpath('//frame[@name="frame-top"]')
            self.driver.switch_to.frame(self.topFrame)

            self.topLeft = self.driver.find_element_by_xpath('//frame[@name="frame-left"]')
            self.driver.switch_to.frame(self.topLeft)
            self.log.info(self.driver.find_element_by_xpath('//body').text)

            self.driver.switch_to.default_content()
            self.log.info("Switched to main frame")
            self.driver.switch_to.frame(self.topFrame)
            self.topMiddle = self.driver.find_element_by_xpath('//frame[@name="frame-middle"]')
            self.driver.switch_to.frame(self.topMiddle)
            self.log.info(self.driver.find_element_by_xpath('//body').text)

            self.driver.switch_to.default_content()
            self.log.info("Switched to main frame")
            self.driver.switch_to.frame(self.topFrame)
            self.topRight = self.driver.find_element_by_xpath('//frame[@name="frame-right"]')
            self.driver.switch_to.frame(self.topRight)
            self.log.info(self.driver.find_element_by_xpath('//body').text)

            self.driver.switch_to.default_content()
            self.bottomFrame = self.driver.find_element_by_xpath('//frame[@name="frame-bottom"]')
            self.driver.switch_to.frame(self.bottomFrame)
            self.log.info(self.driver.find_element_by_xpath('//body').text)

        except:

            self.log.error(sys.exc_info())
            assert False
