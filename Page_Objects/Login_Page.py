import time
from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.login_page_driver = driver
        self.forgot_password_link_locator = "//p[text()='Forgot your password? ']"

    def forgot_password_link_click(self, username_text):
        self.login_page_driver.find_element(By.XPATH, self.forgot_password_link_locator).click()
        

