from selenium import webdriver
from selenium.webdriver.support.select import Select


class CustomerPage:
    # driver = webdriver.Chrome()
    linkCustomer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
    linkCustomer_menu_item_xpath = "//span[@class='menu-item-title'][normalize-space()='Customers']"
    buttonAdd_new_customer_xpath = "//a[normalize-space()='Add new']"
    text_email_id = "Email"
    text_password_id = 'Password'
    text_first_name_id = 'First Name'
    text_last_name_id = 'Last Name'
    radio_gender_female_id = "Gender_Female"
    radio_gender_male_id = "Gender_Male"
    text_date_of_birth_id = "DateOfBirth"
    text_company_name_id = "Company"
    checkbox_is_tax_exempt_id = "IsTaxExempt"
    select_customer_roles_xpath = "//select[@id='SelectedCustomerRoleIds']"
    select_vendor_manager_id = "VendorId"
    text_admin_content_id = "AdminComment"
    button_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def click_customer_menu(self):
        self.driver.find_element_by_xpath(self.linkCustomer_menu_xpath).click()

    def click_customer_menu_item(self):
        self.driver.find_element_by_xpath(self.linkCustomer_menu_item_xpath).click()

    def click_add_new_customer(self):

        self.driver.find_element_by_xpath(self.buttonAdd_new_customer_xpath).click()

    def set_email(self, email):
        # self.driver.find_element_by_id(self.text_email_id).send_keys(Key.clear())
        self.driver.find_element_by_id(self.text_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def set_gender(self, gender):
        if str(gender).lower().strip() == 'female':
            self.driver.find_element_by_id(self.radio_gender_female_id).click()
        else:
            self.driver.find_element_by_id(self.radio_gender_male_id).click()

    def set_date_of_birth(self, dob):
        self.driver.find_element_by_id(self.text_date_of_birth_id).send_keys(dob)

    def set_company_name(self, company):
        self.driver.find_element_by_id(self.text_company_name_id).send_keys(company)

    def check_tax_exempt(self):
        self.driver.find_element_by_id(self.checkbox_is_tax_exempt_id).click()

    def set_customer_roles(self, list1):
        list1 = list(list1)
        select = Select(self.driver.find_element_by_xpath(self.select_customer_roles_xpath))
        if 'Guests' in list1:
            select.select_by_visible_text('Registered').click()
        for i in list1:
            select.select_by_visible_text(i).click()

    def set_vendor_manager(self, vendor):
        select = Select(self.driver.find_element_by_id(self.select_vendor_manager_id))
        select.select_by_visible_text(vendor)

    def click_save(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

    def set_admin_content(self,content):
        self.driver.find_element_by_id(self.text_admin_content_id).send_keys(content)


