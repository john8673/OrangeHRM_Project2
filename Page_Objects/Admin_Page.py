from selenium.webdriver.common.by import By


class Admin_Page:
    def __init__(self, driver):
        self.admin_page_driver = driver
        self.admin_page_locator = "//a[@href='/web/index.php/admin/viewAdminModule']"

        # locators of dropdown elements present in Admin page
        self.user_management_dropdown_locator = "//span[text()='User Management ']"
        self.job_dropdown_locator = "//span[text()='Job ']"
        self.organization_dropdown_locator = "//span[text()='Organization ']"
        self.qualifications_dropdown_locator = "//span[text()='Qualifications ']"
        self.nationalities_dropdown_locator = "//a[text()='Nationalities']"
        self.corporate_branding_dropdown_locator = "//a[text()='Corporate Branding']"
        self.configuration_dropdown_locator = "//span[text()='Configuration ']"

        # locators of various pages mentioned in leftmost of the page
        self.pim_page_locator = "//a[@href='/web/index.php/pim/viewPimModule']"
        self.leave_page_locator = "//a[@href='/web/index.php/leave/viewLeaveModule']"
        self.time_page_locator = "//a[@href='/web/index.php/time/viewTimeModule']"
        self.recruitment_page_locator = "//a[@href='/web/index.php/recruitment/viewRecruitmentModule']"
        self.my_info_page_locator = "//a[@href='/web/index.php/pim/viewMyDetails']"
        self.performance_page_locator = "//a[@href='/web/index.php/performance/viewPerformanceModule']"
        self.dashboard_page_locator = "//a[@href='/web/index.php/dashboard/index']"
        self.directory_page_locator = "//a[@href='/web/index.php/directory/viewDirectory']"
        self.maintenance_page_locator = "//a[@href='/web/index.php/maintenance/viewMaintenanceModule']"
        self.claim_page_locator = "//a[@href='/web/index.php/claim/viewClaimModule']"
        self.buzz_page_locator = "//a[@href='/web/index.php/buzz/viewBuzz']"

    # method to perform click operation of admin page
    def admin_page_click(self):
        self.admin_page_driver.find_element(By.XPATH, self.admin_page_locator).click()

    # method to validate window title of current page
    def admin_page_window_title(self):
        if self.admin_page_driver.title == "OrangeHRM":
            return True

    # methods to validate the dropdown elements present in admin page
    def user_management_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.user_management_dropdown_locator)
        return True

    def job_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.job_dropdown_locator)
        return True

    def organization_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.organization_dropdown_locator)
        return True

    def qualifications_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.qualifications_dropdown_locator)
        return True

    def nationalities_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.nationalities_dropdown_locator)
        return True

    def corporate_branding_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.corporate_branding_dropdown_locator)
        return True

    def configuration_dropdown_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.configuration_dropdown_locator)
        return True

    # methods to validate the various pages mentioned in leftmost of the page
    def admin_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.admin_page_locator)
        return True

    def pim_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.pim_page_locator)
        return True

    def leave_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.leave_page_locator)
        return True

    def time_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.time_page_locator)
        return True

    def recruitment_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.recruitment_page_locator)
        return True

    def my_info_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.my_info_page_locator)
        return True

    def performance_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.performance_page_locator)
        return True

    def dashboard_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.dashboard_page_locator)
        return True

    def directory_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.directory_page_locator)
        return True

    def maintenance_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.maintenance_page_locator)
        return True

    def claim_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.claim_page_locator)
        return True

    def buzz_page_element_validation(self):
        self.admin_page_driver.find_element(By.XPATH, self.buzz_page_locator)
        return True
