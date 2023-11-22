from selenium.webdriver.common.by import By


class Login_Page:
    def __init__(self, driver):
        self.login_page_driver = driver

        # locator for forgot password hyperlink

        self.forgot_password_link_locator = "//p[text()='Forgot your password? ']"

        # locators for login operation attributes

        self.username_textbox_locator = "username"
        self.password_textbox_locator = "password"
        self.login_button_locator = "//button[@type='submit']"

    # method to perform click operation on forgot password hyperlink

    def forgot_password_link_click(self):
        self.login_page_driver.find_element(By.XPATH, self.forgot_password_link_locator).click()

    # methods to perform login operation

    def enter_username(self):
        self.login_page_driver.find_element(By.NAME, self.username_textbox_locator).send_keys("Admin")

    def enter_password(self):
        self.login_page_driver.find_element(By.NAME, self.password_textbox_locator).send_keys("admin123")

    def login_button_click(self):
        self.login_page_driver.find_element(By.XPATH, self.login_button_locator).click()
