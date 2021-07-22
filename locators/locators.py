class MainPageLocators:
    login_button_xpath = "//a[@class='control button2 button2_view_classic button2_size_mail-big button2_theme_mail-white button2_type_link HeadBanner-Button HeadBanner-Button-Enter with-shadow']"

class LoginLocators:
    login_id = "passp-field-login"
    login_button_xpath = "//button[@id='passp:sign-in']"
    password_id = "passp-field-passwd"

class PersonalPageLocators:
    email_subjects_xpath = "//span[@class='mail-MessageSnippet-Item mail-MessageSnippet-Item_subjectWrapper js-message-snippet-subject']/*"
    mail_addresses_xpath = "//span[@class='mail-MessageSnippet-FromText']"
    mail_addresses_attribute = 'title'

class SendingLetterLocators:
    write_letter_button_xpath = "//a[@title='Написать (w, c)']"
    addressee_xpath = "//div[@class='composeYabbles']"
    email_subject_xpath = "//input[@class='composeTextField ComposeSubject-TextField']"
    message_xpath = "//div[@class='cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_htmlplaceholder']"
    send_message_button_xpath = "//div[@class='new__root--3qgLa ComposeControlPanel-Button ComposeControlPanel-Button_new ComposeControlPanel-SendButton ComposeSendButton ComposeSendButton_desktop']/button"
