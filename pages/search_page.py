import allure
from pages.home_page import HomePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchPage(HomePage):

    PAGE_URL = Links.SEARCH_PAGE

    PAGE_HEADING = ("xpath", "//div[@data-testid='large-header']//h1")
    COMMENTS_BUTTON = ("xpath", "//button[@id='comments']")

    @allure.step("Verify that the page heading contains search result.")
    def is_page_heading_contains_search_result(self, text):
        heading_text = self.wait_for_visibility(self.PAGE_HEADING).text
        expected_text = f"Results for “{text}”"
        assert heading_text == expected_text, f"Expected: {expected_text}, but got: {heading_text}."

    @allure.step("Click on the \"Comments\" button.")
    def click_comments_button(self):
        self.click_element(self.COMMENTS_BUTTON)

    def is_opened(self):
        with allure.step(f"Verify that the page with a URL starting with {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    @allure.step("Verify that the task list contains the task.")
    def is_task_list_contains_task(self, task_name):
        task_locator = ("xpath", f"//div[@class='list_holder']//div[contains(text(),'{task_name}')]")
        try:
            self.wait_for_visibility(task_locator)
        except:
            raise TimeoutException(f"The task with name \"{task_name}\" was not found in the task list.")

    @allure.step("Verify that the task list contains the task with comment.")
    def is_task_list_contains_task_with_comment(self, task_name):
        task_locator = ("xpath", f"//div[@aria-labelledby='comments']//span[text()='{task_name}']")
        try:
            self.wait_for_visibility(task_locator)
        except:
            raise TimeoutException(f"The task with name \"{task_name}\" was not found in the task list.")

    @allure.step("Verify that the task list is empty")
    def is_task_list_empty(self, request):
        empty_state_locator = (
            "xpath", f"//div[@class='empty-state-search empty-state tMaqCFY']//div[contains(text(), '{request}')]")
        try:
            self.wait_for_visibility(empty_state_locator)
        except:
            raise TimeoutException("The task list is not empty.")
