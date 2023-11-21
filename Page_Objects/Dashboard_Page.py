from selenium.webdriver.common.by import By


class Dashboard_Page:
    def __init__(self, driver):
        self.dashboard_page_driver = driver

        # locators of logout dropdown elements

        self.account_dropdown_locator = "oxd-userdropdown-tab"
        self.logout_button_locator = "//a[text()='Logout']"

# methods to perform logout operations

    def account_dropdown_click(self):
        self.dashboard_page_driver.find_element(By.CLASS_NAME, self.account_dropdown_locator).click()

    def logout_button_click(self):
        self.dashboard_page_driver.find_element(By.XPATH, self.logout_button_locator).click()
