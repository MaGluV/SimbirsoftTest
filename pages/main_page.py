import pytest
import allure
from SimbirsoftTest.locators.locators import MainPageLocators

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_button_xpath = MainPageLocators.login_button_xpath
		
    @allure.step('Нажимаем на кнопку для входа на страницу авторизации')
    def step_login_button_click(self):
        assert self.driver.find_element_by_xpath(self.login_button_xpath).is_displayed()
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
