import unittest
from selenium import webdriver

from Page_Objects.Admin_Page import Admin_Page
from Page_Objects.Dashboard_Page import Dashboard_Page
from Page_Objects.Login_Page import Login_Page


class AdminPageTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.chrome_driver = webdriver.Chrome()
        self.chrome_driver.maximize_window()
        self.chrome_driver.implicitly_wait(20)
        self.chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        lp_object = Login_Page(self.chrome_driver)
        lp_object.enter_username()
        lp_object.enter_password()
        lp_object.login_button_click()
        ap_object = Admin_Page(self.chrome_driver)
        ap_object.admin_page_click()

    def test_admin_page_title(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.admin_page_window_title()

    def test_is_user_management_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.user_management_dropdown_validation()

    def test_is_job_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.job_dropdown_validation()

    def test_is_organization_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.organization_dropdown_validation()

    def test_is_qualifications_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.qualifications_dropdown_validation()

    def test_is_nationalities_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.nationalities_dropdown_validation()

    def test_is_corporate_branding_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.corporate_branding_dropdown_validation()

    def test_is_configuration_dropdown_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.configuration_dropdown_validation()

    def tearDown(self) -> None:
        dp_object = Dashboard_Page(self.chrome_driver)
        dp_object.account_dropdown_click()
        dp_object.logout_button_click()

