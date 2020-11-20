from selenium import webdriver


class SearchCustomersPage():
    textbox_email_id = "SearchEmail"
    textbox_firstname_id = "SearchFirstName"
    textbox_lastname_id = "SearchLastName"
    button_search_customers_id = "search-customers"
    table_search_results_id = "customers-grid"
    table_rows_xpath = "//table[@id='customers-grid']/tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(last_name)

    def click_search_customers(self):
        self.driver.find_element_by_id(self.button_search_customers_id).click()

    def get_search_email_list(self):
        row_count = len(self.driver.find_elements_by_xpath(self.table_rows_xpath))
        email_list = list()
        for i in range(1, row_count + 1):
            email = self.driver.find_element_by_xpath(
                "//table[@id='customers-grid']/tbody/tr[" + str(i) + "]/td[2]").text
            email_list.append(email)
        return email_list

    def get_search_name_list(self):
        row_count = len(self.driver.find_elements_by_xpath(self.table_rows_xpath))
        email_list = list()
        for i in range(1, row_count + 1):
            email = self.driver.find_element_by_xpath(
                "//table[@id='customers-grid']/tbody/tr[" + str(i) + "]/td[3]").text
            email_list.append(email)
        return email_list
