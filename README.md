**Test Cases Documentation Using Page Object Model in Selenium**

**Overview**

This document outlines the test cases designed for the OrangeHRM website using the Page Object Model (POM) in Selenium. The Page Object Model is employed to enhance test script maintainability, re-usability, and readability by separating the page-specific elements and actions from test logic.

**Project Details:**

Project Name: OrangeHRM_Project2

Tools/Framework Used: Selenium WebDriver, Page Object Model (POM), Unit testing framework.

**Page Objects**

1. Admin_Page file contains the locators of the elements in the Admin page and the methods to, 
i) perform click operation of admin page, ii) validate window title of current page, iii) validate the dropdown elements present in admin page, iv) validate the Main menu elements.

2. Dashboard_Page file contains the locators of logout dropdown elements and the methods to perform logout operations in the Dashboard Page

3. Login_page file contains the locators for login operation attributes and forgot password hyperlink and the methods to perform click operation on forgot password hyperlink and login operations.

4. Reset_Password_Page contains the locators of reset password page and the methods to perform operations in reset password page.

**Test Cases**

1. Admin_Page_Test_Class file contains the testcases to, 
i) validate the title of the admin page, ii) validate dropdown elements present in Admin page Header, iii) validate Main menu elements.

2. Rest_Password_Page_Test_Class file contains the testcase to validate whether the link is successfully sent.

**Test Results**

Test results are attached as HTML file in the directory.


**Conclusion**

The Page Object Model implemented in these test cases helps in maintaining a modular, organized, and scalable test suite. These test cases cover crucial functionalities of the application, ensuring its reliability and functionality.

**NOTE:**
The "ResourceWarning: unclosed file" exception couldn't be handled with this code,

try:

    'The piece of code to be tested'

except ResourceWarning:

    print("Exception handled")"

*I also searched the internet for answers concerning this exception as no files were opened to get sample test data. But I suppose this is because the Page_Objects are imported. Please suggest a way to get around this exception for unclosed file while we open Page Objects files*