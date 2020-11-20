import pytest
# from pytest import fixture
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConf
from Utilities.CustomLogger import CustomLogger
from Utilities.XLUtils import XLUtils


class Test001_ddt_Login:
    BaseUrl = ReadConf.get_BaseUrl()
    path = './/testData/logindata.xlsx'
    xlutil = XLUtils(path)
    row_count = xlutil.get_row_count()
    column_count = xlutil.get_column_count()

    logger = CustomLogger.custom_logger()

    @pytest.mark.regression
    def test_login_ddt(self, set_up):
        self.driver = set_up
        self.driver.get(self.BaseUrl)
        self.log = LoginPage(self.driver)
        list1 = []
        for row in range(2, self.row_count + 1):
            expected_result = self.xlutil.read_data(row, 3)
            self.log.setUserName(self.xlutil.read_data(row, 1))
            self.log.setPassword(self.xlutil.read_data(row, 2))
            self.log.clickLogin()
            actual_title = self.driver.title
            if actual_title == 'Dashboard / nopCommerce administration':
                if expected_result == 'pass':
                    list1.append('pass')
                    self.log.clickLogout()
                    self.logger.info('**pass**')
                elif expected_result == 'fail':
                    list1.append('fail')
                    self.log.clickLogout()
                    self.logger.info('**fail**')
            else:
                if expected_result == 'pass':
                    list1.append('fail')
                    self.logger.info('**fail**')
                elif expected_result == 'fail':
                    list1.append('pass')
                    self.logger.info('**pass**')
        if 'fail' in list1:
            self.logger.info('**** Login DDt test Failed ****')
            self.driver.close()
            assert False
        else:
            self.logger.info('**** Login DDt test Passed ****')
            self.driver.close()
            assert True
