from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys


'''Working fine!'''
class TestFormAuthentication(BaseClass):
    def test_formauthentication(self):
        try:
            self.log=self.getLogger()
            self.form_auth=HomePage(self.driver)
            self.form_auth.home("Form Authentication",5)
            self.driver.find_element_by_xpath('//input[@name="username"]').send_keys("tomsmith")
            self.driver.find_element_by_xpath('//input[@name="password"]').send_keys("SuperSecretPassword!")
            self.driver.find_element_by_xpath('//button[@type="submit"]').click()
            self.driver.implicitly_wait(10)
            if "You logged into a secure area!" in self.driver.find_element_by_xpath('//div[@class="flash success"]').text:
                self.log.info("Logged in successfully!")
                self.driver.find_element_by_xpath('//a[@class="button secondary radius"]').click()
                self.driver.implicitly_wait(10)
                if "You logged out of the secure area!" in self.driver.find_element_by_xpath('//div[@class="flash success"]').text:
                    self.log.info("Logged out successfully!")
                else:
                    self.log.critical("Error while logging out")


            else:
                self.log.critical("There was error in logging in")

        except:
            self.log.error(sys.exc_info())
            assert False