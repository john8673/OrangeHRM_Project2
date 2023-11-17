import time
from selenium.webdriver.common.by import By


class Reset_Password_Page:
    def __init__(self, driver):
        self.reset_password_page_driver = driver
        self.username_textbox_locator = "username"
        self.reset_password_button_locator = "//button[text()=' Reset Password ']"
        self.link_sent_successfully_text_locator = "//p[text()='A reset password link has been sent to you via email.']"

    def enter_username(self):
        self.reset_password_page_driver.find_element(By.NAME, self.username_textbox_locator).send_keys("WalterWhite")

    def reset_password_button_click(self):
        self.reset_password_page_driver.find_element(By.XPATH, self.reset_password_button_locator).click()

    def link_sent_successfully_text(self):
        self.reset_password_page_driver.find_element(By.XPATH, self.link_sent_successfully_text_locator)
