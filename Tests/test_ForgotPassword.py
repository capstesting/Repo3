from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys

class TestForgotPass(BaseClass):
    def test_forgot_pass(self):
        try:
            self.log=self.getLogger()
            self.forgot=HomePage(self.driver)
            self.forgot.home("Forgot Password",10)
            self.driver.find_element_by_xpath('//input[@id="email"]').send_keys("anc@gmail.com")
            self.driver.find_element_by_xpath('//button[@id="form_submit"]').click()
            if "Internal Server Error" in self.driver.find_element_by_xpath("//h1").text:
                self.log.warning("The following error occured: "+self.driver.find_element_by_xpath("//h1").text)

        except:
            self.log.error(sys.exc_info())
            assert False