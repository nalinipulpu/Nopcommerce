import time

# from selenium import webdriver
import pytest

from pageObjects.SearchCustumersPage import SearchCustomersPage
from pageObjects.CustomerPage import CustomerPage
from pageObjects.LoginPage import LoginPage
from Utilities.CustomLogger import CustomLogger
from Utilities.ReadProperties import ReadConf


class TestSearchCustomer:
    logger = CustomLogger.custom_logger()
    id = ReadConf.get_UserId()
    password = ReadConf.get_Password()
    # driver=webdriver.Chrome()
    logger.info('************ TestSearchcustomer started ************')

    @pytest.mark.regression
    def test_search_customer_by_email(self, set_up):
        self.logger.info('************ test_search_customer_by_email started ************')
        self.driver = set_up
        self.logger.info('************ Entering Login Details ************')
        lp = LoginPage(self.driver)
        lp.setUserName(self.id)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        cust_page = CustomerPage(self.driver)
        try:
            cust_page.click_customer_menu()
            self.logger.info("*******  login successful *********")

        except:
            print('login failed')
            self.logger.info("*******  login failed *********")
        time.sleep(2)
        cust_page.click_customer_menu_item()
        search_cust = SearchCustomersPage(self.driver)
        email = 'brenda_lindgren@nopCommerce.com'
        self.logger.info('****** entering search email id ******')
        search_cust.set_email('brenda_lindgren@nopCommerce.com')
        search_cust.click_search_customers()
        time.sleep(5)
        email_list = search_cust.get_search_email_list()
        if email in email_list:
            self.logger.info('****** custumer email_id is found ******')
            self.logger.info('****** test_search_customer_by_email is passed ******')
            assert True
            self.driver.close()
        else:
            self.logger.info('****** test_search_customer_by_email is failed ******')
            # self.driver.save_screenshot()
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_search_customer_by_name(self, set_up):
        self.logger.info('************ test_search_customer_by_name started ************')
        self.driver = set_up
        self.logger.info('************ Entering Login Details ************')
        lp = LoginPage(self.driver)
        lp.setUserName(self.id)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        cust_page = CustomerPage(self.driver)
        try:
            cust_page.click_customer_menu()
            self.logger.info("*******  login successful *********")

        except:
            print('login failed')
            self.logger.info("*******  login failed *********")
        time.sleep(2)
        cust_page.click_customer_menu_item()
        search_cust = SearchCustomersPage(self.driver)
        name = 'James Pan'
        first_name=name.split()[0]
        last_name=name.split()[1]
        self.logger.info('****** entering search name ******')
        search_cust.set_first_name(first_name)
        search_cust.set_last_name(last_name)
        search_cust.click_search_customers()
        time.sleep(5)
        name_list = search_cust.get_search_name_list()
        if name in name_list:
            self.logger.info('****** custumer email_id is found ******')
            self.logger.info('****** test_search_customer_by_name is passed ******')
            assert True
            self.driver.close()
        else:
            self.logger.info('****** test_search_customer_by_name is failed ******')
            # self.driver.save_screenshot()
            self.driver.close()
            assert False
