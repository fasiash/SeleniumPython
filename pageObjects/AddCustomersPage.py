import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add Customer Page
    linkCustomer_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    linkCustomer_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    AddNew_Button_text_xpath = "(//a[normalize-space()='Add new'])[1]"
    Email_text_xpath = "//input[@id='Email']"
    password_text_xpath = "//input[@id='Password']"
    firstname_text_xpath = "//input[@id='FirstName']"
    lastname_text_xpath = "//input[@id='LastName']"
    gender_male_xpath = "//input[@id='Gender_Male']"
    gender_female_xpath = "//input[@id='Gender_Female']"
    dateOfBirth_text_xpath = "//input[@id='DateOfBirth']"
    companyName_text_xpath = "//input[@id='Company']"
    taxExempted_checkbox_Xpath = "//input[@id='IsTaxExempt']"
    newLetter_text_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    list_customerRoles_text_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    listItem_Administrator_xpath = "//span[normalize-space()='Administrators']"
    listItem_Moderators_xpath = "//span[normalize-space()='Forum Moderators']"
    listItem_guests_xpath = "//span[normalize-space()='Guests']"
    listItem_registered_xpath = "//span[normalize-space()='Registered']"
    listItem_vendors_xpath = "//span[normalize-space()='Vendors']"
    dropItem_vendor_xpath = "//select[@id='VendorId']"
    list_Manager_vendor_text_xpath = "//select[@id='VendorId']"
    active_checkbox_xpath = "//input[@id='Active']"
    admin_text_xpath = "//textarea[@id='AdminComment']"
    save_button_xpath = "//button[@name='save']"
    customer_info_icon = "//div[@class='card-title']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.linkCustomer_menu_item_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.AddNew_Button_text_xpath).click()

    def ClickOnCustomerIcon(self):
        self.driver.find_element(By.XPATH, self.customer_info_icon).click()

    def set_email(self, email):
        self.driver.find_element(By.XPATH, self.Email_text_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_text_xpath).send_keys(password)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH, self.list_customerRoles_text_xpath).click()
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.listItem_registered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.listItem_Administrator_xpath)
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.listItem_guests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.listItem_registered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.listItem_vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.listItem_guests_xpath)
        time.sleep(3)
        # self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.dropItem_vendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.gender_male_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.gender_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.gender_male_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.firstname_text_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH, self.lastname_text_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.dateOfBirth_text_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH, self.companyName_text_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.admin_text_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()
