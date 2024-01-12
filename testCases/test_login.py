import time

import allure
import pytest

from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperty import ReadConfig

allure.severity(severity_level="Normal")


@pytest.mark.run(order=1)
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******Test_001_Login********")
        self.logger.info("*****Verifying Homepage title********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            time.sleep(2)
            self.driver.close()
            self.logger.info("******HomePage title is passed********")
        else:
            self.driver.save_screenshot("C:\\Users\\Codetru\\PycharmProjects\\nopCommerceApp\\Screenshots" + "test_homePageTitle.png")
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_file("LoginIssue.PNG"))
            self.driver.close()
            self.logger.error("******homePage title is failed********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******Verifying Login test********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("******login test is passed********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("******login test is failed********")
            assert False
