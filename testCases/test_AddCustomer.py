import string
import time
from datetime import datetime
import random

import pytest
from selenium import webdriver
from Utilities.ReadProperties import ReadConf
from pageObjects.LoginPage import LoginPage
from pageObjects.CustomerPage import CustomerPage
from Utilities.CustomLogger import CustomLogger


class Test_003_AddCustomer():
    # driver = webdriver.Chrome()
    logger = CustomLogger.custom_logger()
    screen_shots_file_path = 'C:\\Users\\nalin\\PycharmProjects\\pythonProject3\\screenshots\\'

    @pytest.mark.sanity
    def test_add_customer(self, set_up):
        self.driver = set_up
        lp = LoginPage(self.driver)
        lp.setUserName(ReadConf.get_UserId())
        lp.setPassword(ReadConf.get_Password())
        lp.clickLogin()
        self.logger.info("***********  Login Successful ***********")
        self.logger.info("*********** Test_003_customer started **********")

        custpage = CustomerPage(self.driver)
        self.logger.info("*********** filling the form details **********")
        custpage.click_customer_menu()
        time.sleep(2)
        custpage.click_customer_menu_item()
        custpage.click_add_new_customer()
        email = self.create_random_user_id() + '@gmail.com'
        custpage.set_email(email)
        custpage.set_password('selenium')
        custpage.set_gender('female')
        custpage.set_date_of_birth('7/09/1990')
        custpage.set_company_name('oracle')
        # custpage.set_customer_roles(['Administrator'])
        custpage.set_vendor_manager('Vendor 2')
        custpage.set_admin_content('this isn a new customer added by nalini')
        self.logger.info("*********** saving customer data *********************")
        custpage.click_save()
        time.sleep(3)

        body_text = self.driver.find_element_by_tag_name('body').text
        expected_text = 'The new customer has been added successfully.'
        self.logger.info("************* validating customer add **************")
        if expected_text in body_text:
            self.logger.info('************ Test_003_customer passed **********  ')
            assert True
            self.driver.close()
        else:
            self.logger.info('************ Test_003_customer failed **********  ')
            timestamp = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
            self.driver.save_screenshot(self.screen_shots_file_path + timestamp + 'test_AddCustomer.png')

            self.driver.close()
            assert False
        self.logger.info('************ Test_003_customer completed **********  ')

    def create_random_user_id(self):
        size, char = 8, string.ascii_lowercase + string.digits
        return ''.join(random.choice(char) for x in range(size))
