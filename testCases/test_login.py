import pytest
# from pytest import fixture
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.ReadProperties import ReadConf
from Utilities.CustomLogger import CustomLogger


class Test001Login:
    BaseUrl = ReadConf.get_BaseUrl()
    UserId = ReadConf.get_UserId()
    Password = ReadConf.get_Password()
    logger = CustomLogger.custom_logger()

    @pytest.mark.regression
    def test_homepage_title(self, set_up):

        self.logger.info('********  Test_001Login test started *******')
        self.logger.info('******** test_homepage_title started *******')
        self.driver = set_up
        self.driver.get(self.BaseUrl)
        actual_title = self.driver.title

        if actual_title == 'Your tore. Login':
            assert True
            self.logger.info('******** test test_homepage_title is passed *******')
            self.driver.close()

        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_HomePageTitle.png')
            self.logger.error('******** test_homepage_title is failed *******')
            self.driver.close()
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity

    def test_login(self, set_up):
        self.driver = set_up
        self.driver.get(self.BaseUrl)
        self.log = LoginPage(self.driver)
        self.log.setUserName(self.UserId)
        self.log.setPassword(self.Password)
        self.log.clickLogin()
        actual_title = self.driver.title
        # self.log.button_logout_link_text

        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info('******** test_Login is passed *******')

        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_Login.png')
            self.logger.error('******** test_Login is failed *******')
            self.driver.close()
            assert False
