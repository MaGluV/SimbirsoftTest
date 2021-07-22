import pytest
import allure
from locators import SendingLetterLocators

class SendingLetterPage:

    def __init__(self, driver):
        self.driver = driver
        self.write_letter_button_xpath = SendingLetterLocators.write_letter_button_xpath
        self.addressee_xpath = SendingLetterLocators.addressee_xpath
        self.email_subject_xpath = SendingLetterLocators.email_subject_xpath
        self.message_xpath = SendingLetterLocators.message_xpath
        self.send_message_button_xpath = SendingLetterLocators.send_message_button_xpath

    @allure.step('Нажимаем на кнопку для создания письма')
    def step_write_letter_click(self):
        assert self.driver.find_element_by_xpath(self.write_letter_button_xpath).is_displayed()
        self.driver.find_element_by_xpath(self.write_letter_button_xpath).click()

    @allure.step('Вводим адрес')		
    def step_enter_address(self, address):
        self.driver.find_element_by_xpath(self.addressee_xpath).clear()
        self.driver.find_element_by_xpath(self.addressee_xpath).send_keys(address)
        assert self.driver.find_element_by_xpath(self.addressee_xpath).is_displayed()

    @allure.step('Указываем тему письма')		
    def step_enter_subject(self, subject):
        self.driver.find_element_by_xpath(self.email_subject_xpath).click()
        self.driver.find_element_by_xpath(self.email_subject_xpath).send_keys(subject)
        assert self.driver.find_element_by_xpath(self.addressee_xpath).is_displayed()

    @allure.step('Пишем текст письма')		
    def step_enter_message(self, message):
        assert self.driver.find_element_by_xpath(self.message_xpath).is_displayed()
        self.driver.find_element_by_xpath(self.message_xpath).click()
        self.driver.find_element_by_xpath(self.message_xpath).send_keys(message)

    @allure.step('Нажимаем на кнопку для отправки письма')		
    def step_send_letter(self):
        assert self.driver.find_element_by_xpath(self.send_message_button_xpath).is_displayed()
        self.driver.find_element_by_xpath(self.send_message_button_xpath).click()
