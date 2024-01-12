import time

import allure
import pytest
from allure_commons.types import AttachmentType

from pageObjects.LoginPage import Login
from pageObjects.AddCustomersPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperty import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.run(order=5)
class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    allure.severity(severity_level="Major")

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(2)
        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("gfxqcrvl@gmail.com")
        searchcust.clickSearch()
        time.sleep(4)
        status=searchcust.searchCustomerByEmail("gfxqcrvl@gmail.com")
        time.sleep(2)
        assert True==status
        self.driver.close()
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")