import sys
from time import sleep
from utilities.BaseClass import BaseClass


class TestAB(BaseClass):
    def test_ab(self):
        log = self.getLogger254()
        try:
            self.driver.find_element_by_xpath('//a[text()="A/B Testing"]').click()
            sleep(5)
            self.WaitUntil(10, 'h3')
            message = self.driver.find_element_by_tag_name('p').text
            if 'Also known as' in message:
                log.info("First Test is successfully executed.")

        except:
            log.error(sys.exc_info())
