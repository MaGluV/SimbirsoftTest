#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from locators import MainPageLocators

class MainPage:
	
	def __init__(self, driver):
		self.driver = driver
		self.login_button_xpath = MainPageLocators.login_button_xpath
		
	def login_button_click(self):
		self.driver.find_element_by_xpath(self.login_button_xpath).click()
