#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import allure
import pytest
from locators import LoginLocators

class LoginPage:
	
	def __init__(self, driver):
		self.driver = driver
		self.login_id = LoginLocators.login_id
		self.login_button_xpath = LoginLocators.login_button_xpath
		self.password_id = LoginLocators.password_id
		self.password_button_xpath = LoginLocators.password_button_xpath
		
	@allure.step('Вводим адрес')	
	def step_enter_mail(self, mail):
		self.driver.find_element_by_id(self.login_id).clear()
		self.driver.find_element_by_id(self.login_id).send_keys(mail)
		assert self.driver.find_element_by_id(self.login_id).is_displayed()
		
	@allure.step('Нажимаем на кнопку для ввода пароля')	
	def step_click_login(self):
		assert self.driver.find_element_by_xpath(self.login_button_xpath).is_displayed()
		self.driver.find_element_by_xpath(self.login_button_xpath).click()
		
	@allure.step('Вводим пароль')
	def step_enter_password(self, password):
		self.driver.find_element_by_id(self.password_id).clear()
		self.driver.find_element_by_id(self.password_id).send_keys(password)
		assert self.driver.find_element_by_id(self.password_id).is_displayed()

	@allure.step('Нажимаем на кнопку для авторизации')
	def step_click_password(self):
		assert self.driver.find_element_by_xpath(self.password_button_xpath).is_displayed()
		self.driver.find_element_by_xpath(self.password_button_xpath).click()
	
