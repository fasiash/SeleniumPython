import time

import allure
import pytest

from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities import ExcelUtility
from utilities.customLogger import LogGen
from utilities.readProperty import ReadConfig

allure.severity(severity_level="Normal")


@pytest.mark.run(order=2)
class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\Codetru\\PycharmProjects\\nopCommerceApp\\testData\\TestData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********Test_002_DDT_Login******")
        self.logger.info("******Verifying Login  ddt test********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows = ExcelUtility.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in excel:", self.rows)

        lst_status = []  # empty list

        for r in range(2, self.rows + 1):
            self.user = ExcelUtility.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtility.readData(self.path, 'Sheet1', r, 2)
            self.expected = ExcelUtility.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)
            act_title = self.driver.title
            print(act_title)
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("***Failed***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("***Failed***")

                    lst_status.append("Pass")
                elif self.expected == "Fail":
                    self.logger.info("***Passed***")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("***Login DDt test passed***")
            time.sleep(2)
            self.driver.close()
            assert True
        else:
            self.logger.info("***Login DDT test failed***")
            time.sleep(2)
            self.driver.close()
            assert False
        self.logger.info("***End of Login DDT test failed***")
        self.logger.info("***Completed Test_002_DDT_Login***")
