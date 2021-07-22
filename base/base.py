import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Base:
    
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.TEST_TIMEOUT = 20
        self.NODE_URL = 'http://127.0.0.1:4444/wd/hub'
        self.CAPABILITIES = {
                'browserName':'firefox',
                'javascriptEnabled':True}
        self.driver = webdriver.Remote(
            command_executor=self.NODE_URL,
            desired_capabilities=self.CAPABILITIES)
        self.driver.implicitly_wait(self.TEST_TIMEOUT)
        self.driver.get("https://mail.yandex.ru/")
        self.driver.maximize_window()
		
        yield self.driver
        if self.driver is not None:
            self.driver.close()

	
	
