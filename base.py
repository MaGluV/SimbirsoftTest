#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Base:

	@pytest.fixture(autouse=True)
	def set_up(self):
		print("Initiating Firefox driver")
		self.driver = webdriver.Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities={
				'browserName':'firefox',
				'javascriptEnabled':True})
		print("Test is started")
		self.driver.implicitly_wait(10)
		self.driver.get("https://mail.yandex.ru/")
		self.driver.maximize_window()
		
		yield self.driver
		if self.driver is not None:
			print("-----------------------------------------")
			print("Tests is finished")
			self.driver.close()
			#self.driver.quit()
			#,DesiredCapabilities.FIREFOX

	
	
