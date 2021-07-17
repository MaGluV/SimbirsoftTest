#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MainPageLocators:
	login_button_xpath = "/html/body/div/div/div[2]/div/div/div[4]/a[2]"
	
class LoginLocators:
	login_id = "passp-field-login"
	login_button_xpath = "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[3]/button"
	password_id = "passp-field-passwd"
	password_button_xpath = "/html/body/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/form/div[3]/button"
	
class PersonalPageLocators:
	email_subjects_xpath = "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subjectWrapper js-message-snippet-subject']/*"
	mail_addresses_xpath = "//span[@class='mail-MessageSnippet-FromText']"
	mail_addresses_attribute = 'title'
	
class SendingLetterLocators:
	write_letter_button_xpath = "//a[@title='Написать (w, c)']"
	addressee_xpath = "//div[@class='composeYabbles']"
	email_subject_xpath = "//input[@class='composeTextField ComposeSubject-TextField']"
	message_xpath = "//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_htmlplaceholder']"
	send_message_button_xpath = "//button[@class='control button2 button2_view_default button2_tone_default button2_size_l button2_theme_normal button2_pin_circle-circle ComposeControlPanelButton-Button ComposeControlPanelButton-Button_sidePadding']"
