import allure
from base.base_page import BasePage
from config.links import Links


class AccountDeletedPage(BasePage):

    PAGE_URL = Links.ACCOUNT_DELETED_PAGE

    ACCOUNT_DELETED_HEADING = ("xpath", "//h1[text()='Account deleted']")

    @allure.step("Verify that the page heading is \"Account deleted\".")
    def is_page_heading_account_deleted(self):
        heading_element = self.wait_for_visibility(self.ACCOUNT_DELETED_HEADING)
        assert heading_element.text == "Account deleted", \
            f"Expected page heading \"Account deleted\" but got \"{heading_element.text}\"."
