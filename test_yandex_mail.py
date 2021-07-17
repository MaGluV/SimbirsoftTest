#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import pytest
from base import Base
from main_page import MainPage
from login_page import LoginPage
from personal_page import PersonalPage
from sending_letter_page import SendingLetterPage

@pytest.mark.usefixtures('set_up')
class TestYandexMail(Base):

	def test_yandex_mail(self):
		driver = self.driver
		main = MainPage(driver)
		main.login_button_click()
		time.sleep(10)
		assert driver.title.count('Авторизация') == 1, "Login title is wrong"
		
		login = LoginPage(driver)
		login.enter_mail("smbrtest1@yandex.ru")
		login.click_login()
		time.sleep(2)
		login.enter_password("rnRMLmViir6H9Lv")
		login.click_password()
		time.sleep(10)
		assert driver.title.count('Входящие') == 1, "Personal page title is wrong"
		
		personal = PersonalPage(driver)
		subjects = personal.scan_subjects()
		addresses = personal.scan_addresses()
		letters = personal.find_letters_by_subject(subjects,addresses, "Simbirsoft Тестовое задание")
		assert letters[1] == 3, "Number of letters is wrong"
		
		sendingLetter = SendingLetterPage(driver)
		for test_address in letters[0]:
			sendingLetter.write_letter_click()
			time.sleep(3)
			sendingLetter.enter_address(test_address)
			time.sleep(2)
			sendingLetter.enter_subject("Simbirsoft Тестовое задание. Глушков")
			time.sleep(2)
			sendingLetter.enter_message(str(letters[1]))
			time.sleep(2)
			sendingLetter.send_letter()
			time.sleep(10)
			assert driver.title.count('Входящие') == 1, "Sending letter page title is wrong"
			
		
		
		
		
		
		
		





