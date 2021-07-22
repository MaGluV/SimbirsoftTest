#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import allure
import pytest
from base import Base
from main_page import MainPage
from login_page import LoginPage
from personal_page import PersonalPage
from sending_letter_page import SendingLetterPage

@pytest.mark.usefixtures('set_up')
class TestYandexMail(Base):

	@allure.feature("Yandex mail test")
	@allure.story("Тестирование Яндекс почты")
	@allure.severity(allure.severity_level.NORMAL)
	def test_yandex_mail(self):
		driver = self.driver
		main = MainPage(driver)
		main.step_login_button_click()
		time.sleep(10)
		#assert driver.title.count('Авторизация') == 1, "Login title is wrong"
		
		login = LoginPage(driver)
		login.step_enter_mail("smbrtest1@yandex.ru")
		login.step_click_login()
		time.sleep(2)
		login.step_enter_password("rnRMLmViir6H9Lv")
		login.step_click_password()
		time.sleep(10)
		#assert driver.title.count('Входящие') == 1, "Personal page title is wrong"
		
		personal = PersonalPage(driver)
		subjects = personal.step_scan_subjects()
		addresses = personal.step_scan_addresses()
		letters = personal.step_find_letters_by_subject(subjects,addresses, "Simbirsoft Тестовое задание")
		#assert letters[1] == 3, "Number of letters is wrong"
		
		sendingLetter = SendingLetterPage(driver)
		for test_address in letters[0]:
			sendingLetter.step_write_letter_click()
			time.sleep(3)
			sendingLetter.step_enter_address(test_address)
			time.sleep(2)
			sendingLetter.step_enter_subject("Simbirsoft Тестовое задание. Глушков")
			time.sleep(2)
			sendingLetter.step_enter_message(str(letters[1]))
			time.sleep(2)
			sendingLetter.step_send_letter()
			time.sleep(10)
			#assert driver.title.count('Входящие') == 1, "Sending letter page title is wrong"
			
		
		
		
		
		
		
		





