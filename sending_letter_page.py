#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from locators import SendingLetterLocators

class SendingLetterPage:
	
	def __init__(self, driver):
		self.driver = driver
		self.write_letter_button_xpath = SendingLetterLocators.write_letter_button_xpath
		self.addressee_xpath = SendingLetterLocators.addressee_xpath
		self.email_subject_xpath = SendingLetterLocators.email_subject_xpath
		self.message_xpath = SendingLetterLocators.message_xpath
		self.send_message_button_xpath = SendingLetterLocators.send_message_button_xpath

	def write_letter_click(self):
		self.driver.find_element_by_xpath(self.write_letter_button_xpath).click()
		
	def enter_address(self, address):
		self.driver.find_element_by_xpath(self.addressee_xpath).clear()
		self.driver.find_element_by_xpath(self.addressee_xpath).send_keys(address)
		
	def enter_subject(self, subject):
		self.driver.find_element_by_xpath(self.email_subject_xpath).click()
		self.driver.find_element_by_xpath(self.email_subject_xpath).send_keys(subject)
		
	def enter_message(self, message):
		self.driver.find_element_by_xpath(self.message_xpath).click()
		self.driver.find_element_by_xpath(self.message_xpath).send_keys(message)
		
	def send_letter(self):
		self.driver.find_element_by_xpath(self.send_message_button_xpath).click()
		
		
		
		
