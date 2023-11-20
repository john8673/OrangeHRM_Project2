from selenium import webdriver
import unittest

from Page_Objects.Login_Page import Login_Page
from Page_Objects.Reset_Password_Page import Reset_Password_Page


class LoginPageTestCase(unittest.TestCase):

    def test_forgot_password_link(self):
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.maximize_window()
        self.chrome_driver.implicitly_wait(20)
        self.chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        lp_object = Login_Page(self.chrome_driver)
        lp_object.forgot_password_link_click()
        rp_object = Reset_Password_Page(self.chrome_driver)
        rp_object.enter_username()
        rp_object.reset_password_button_click()
        assert rp_object.link_sent_successfully_text()

