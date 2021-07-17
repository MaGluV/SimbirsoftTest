#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from locators import LoginLocators

class LoginPage:
	
	def __init__(self, driver):
		self.driver = driver
		self.login_id = LoginLocators.login_id
		self.login_button_xpath = LoginLocators.login_button_xpath
		self.password_id = LoginLocators.password_id
		self.password_button_xpath = LoginLocators.password_button_xpath
		
	def enter_mail(self, mail):
		self.driver.find_element_by_id(self.login_id).clear()
		self.driver.find_element_by_id(self.login_id).send_keys(mail)
		
	def click_login(self):
		self.driver.find_element_by_xpath(self.login_button_xpath).click()
		
	def enter_password(self, password):
		self.driver.find_element_by_id(self.password_id).clear()
		self.driver.find_element_by_id(self.password_id).send_keys(password)

	def click_password(self):
		self.driver.find_element_by_xpath(self.password_button_xpath).click()
	
