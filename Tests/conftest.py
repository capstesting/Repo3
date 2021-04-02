from selenium import webdriver
import pytest
from time import sleep


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path='E:\Python\Selenium\chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/')
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()




