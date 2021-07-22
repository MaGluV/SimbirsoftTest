#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import allure
import pytest
from locators import PersonalPageLocators

class PersonalPage:
	
	def __init__(self, driver):
		self.driver = driver
		self.email_subjects_xpath = PersonalPageLocators.email_subjects_xpath
		self.mail_addresses_xpath = PersonalPageLocators.mail_addresses_xpath
		self.mail_addresses_attribute = PersonalPageLocators.mail_addresses_attribute
		
	@allure.step('Ищем названия писем')
	def step_scan_subjects(self):
		subjects = []
		assert len(self.driver.find_elements_by_xpath(self.email_subjects_xpath)) != 0
		for title in self.driver.find_elements_by_xpath(self.email_subjects_xpath):
			subjects.append(title.text)
		return subjects
	
	@allure.step('Ищем адреса')	
	def step_scan_addresses(self):
		addresses = [] 
		assert len(self.driver.find_elements_by_xpath(self.mail_addresses_xpath)) != 0
		for address in self.driver.find_elements_by_xpath(self.mail_addresses_xpath):
			addresses.append(address.get_attribute(self.mail_addresses_attribute))
		return addresses
	
	@allure.step('Считаем количество писем с указанным названием')
	def step_find_letters_by_subject(self, subjects, addresses, subject):
		letters = [[subjects[2*i],subjects[2*i+1],addresses[i]] for i in range(len(addresses))]
		number_of_letters = 0
		test_address = []
		for letter in letters:
			if letter[0].count(subject) == 1 :
				test_address.append(letter[2])
				number_of_letters += int(letter[1]) if letter[1] != '' else 1
		test_addresses = list(set(test_address))
		assert number_of_letters == 3
		return test_addresses,number_of_letters
	
