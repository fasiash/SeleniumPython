import time

import allure
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCustomersPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperty import ReadConfig
from utilities.customLogger import LogGen

allure.severity(severity_level="critical")


@pytest.mark.run(order=4)
class Test_005_SearchCustomerByName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")
        time.sleep(2)
        self.addcust = AddCustomer(self.driver)
        time.sleep(2)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("mohammed")
        searchcust.setLastName("Fasiuddin")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("mohammed Fasiuddin")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")