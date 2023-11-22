import unittest

from selenium import webdriver

from Page_Objects.Admin_Page import Admin_Page
from Page_Objects.Dashboard_Page import Dashboard_Page
from Page_Objects.Login_Page import Login_Page


class AdminPageTestCase(unittest.TestCase):

    # setup method, to be executed before each testcase begins

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

    # testcase to validate the title of the current window
    def test_admin_page_title(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.admin_page_window_title()

    # From line 31 to line 57, testcases to validate dropdown elements present in Admin page Header
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

    # From line 61 to line 107, testcases to validate Main menu elements

    def test_is_admin_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.admin_page_element_validation()

    def test_is_pim_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.pim_page_element_validation()

    def test_is_leave_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.leave_page_element_validation()

    def test_is_time_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.time_page_element_validation()

    def test_is_recruitment_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.recruitment_page_element_validation()

    def test_is_my_info_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.my_info_page_element_validation()

    def test_is_performance_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.performance_page_element_validation()

    def test_is_dashboard_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.dashboard_page_element_validation()

    def test_is_directory_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.directory_page_element_validation()

    def test_is_maintenance_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.maintenance_page_element_validation()

    def test_is_claim_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.claim_page_element_validation()

    def test_is_buzz_page_element_present(self):
        ap_object = Admin_Page(self.chrome_driver)
        assert ap_object.buzz_page_element_validation()

    # teardown method, to be executed after each testcase completes

    def tearDown(self) -> None:
        dp_object = Dashboard_Page(self.chrome_driver)
        dp_object.account_dropdown_click()
        dp_object.logout_button_click()
