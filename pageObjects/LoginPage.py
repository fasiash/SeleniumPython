import allure
from selenium.webdriver.common.by import By

allure.severity(severity_level="Normal")


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_Login_Xpath = "//button[@type='submit']"
    link_Logout_linktest = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_Xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Logout_linktest).click()
