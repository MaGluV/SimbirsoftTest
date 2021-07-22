import pytest
import allure
from .base.base import Base
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.personal_page import PersonalPage
from .pages.sending_letter_page import SendingLetterPage

@pytest.mark.usefixtures('set_up')
class TestYandexMail(Base):

    @allure.feature("Yandex mail test")
    @allure.story("Тестирование Яндекс почты")
    @allure.severity(allure.severity_level.NORMAL)
    def test_yandex_mail(self):
        driver = self.driver
        main = MainPage(driver)
        main.step_login_button_click()
		
        login = LoginPage(driver)
        login.step_enter_mail("smbrtest1@yandex.ru")
        login.step_click_login()
        login.step_enter_password("rnRMLmViir6H9Lv")
        login.step_click_password()

        personal = PersonalPage(driver)
        subjects = personal.step_scan_subjects()
        addresses = personal.step_scan_addresses()
        letters = personal.step_find_letters_by_subject(subjects,addresses, "Simbirsoft Тестовое задание")

        sendingLetter = SendingLetterPage(driver)
        for test_address in letters[0]:
            sendingLetter.step_write_letter_click()
            sendingLetter.step_enter_address(test_address)
            sendingLetter.step_enter_subject("Simbirsoft Тестовое задание. Глушков")
            sendingLetter.step_enter_message(str(letters[1]))
            sendingLetter.step_send_letter()
