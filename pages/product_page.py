from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*self.locators.ADD_BUTTON)
        add_button.click()

    def should_be_add_button(self):
        assert self.element_is_visible(self.locators.ADD_BUTTON), "Add button is not presented"

    def should_be_success_message(self):
        assert self.element_is_visible(self.locators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_product_name(self):
        assert self.element_is_visible(self.locators.PRODUCT_NAME), "Product name is not presented"

    def should_be_added_product_name_in_success_message(self):
        assert self.element_is_visible(self.locators.ADDED_PRODUCT_NAME), "Added product name is not presented in " \
                                                                          "success message "

    def should_be_product_price(self):
        assert self.element_is_visible(self.locators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_added_product_price_in_success_message(self):
        assert self.element_is_visible(self.locators.ADDED_PRODUCT_PRICE), "Added product price is not presented in " \
                                                                          "success message"

    def should_be_added_correct_product(self):
        product_name = self.browser.find_element(*self.locators.PRODUCT_NAME).text
        added_product_name = self.browser.find_element(*self.locators.ADDED_PRODUCT_NAME).text
        assert product_name == added_product_name, "Product names are not equal"

    def should_be_added_correct_price(self):
        product_price = self.browser.find_element(*self.locators.PRODUCT_PRICE).text
        added_product_price = self.browser.find_element(*self.locators.PRODUCT_PRICE).text
        assert product_price == added_product_price, "Product price are not equal"
