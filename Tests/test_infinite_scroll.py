from time import sleep
from PageObjects.home import HomePage
from utilities.BaseClass import BaseClass
import sys


class TestInfiniteScroll(BaseClass):
    '''Class for infinite scroll'''

    def test_infinite_class(self):
        '''Method for infinite scroll'''
        try:
            self.log = self.getLogger()
            self.scroll = HomePage(self.driver)
            self.scroll.home("Infinite Scroll", 5)
            self.scroll_time = 2
            self.last_height = self.driver.execute_script("return document.body.scrollHeight")
            self.count = 1

            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                self.log.info("Scrolled " + str(self.count) + " times")
                self.count += 1
                sleep(self.scroll_time)
                self.new_height = self.driver.execute_script("return document.body.scrollHeight")
                if self.new_height == self.last_height or self.count == 15:
                    break

                self.last_height = self.new_height


        except:
            self.log.error(sys.exc_info())
            assert False
