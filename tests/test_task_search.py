import allure
import random
import pytest
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator
from utils.screenshot import take_screenshot

@allure.feature("Task Search")
class TestTaskSearch(BaseTest):

    @pytest.mark.order(31)
    @pytest.mark.regression
    @allure.description("""
    This test verifies that a user can successfully search for a task by its exact name, ensuring that the correct task is displayed in the search results.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC31: Successful search for a task by its name.")
    def test_task_search_by_name(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        try:
            # Steps:
            self.home_page.click_search_button()
            self.home_page.enter_search_request(task_name)
            self.home_page.is_search_results_section_contains_task(task_name)
            self.home_page.click_on_search_result(task_name)
            self.task_page.is_opened()
        except Exception as e:
            take_screenshot(self.driver, "Task Search by Name Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @pytest.mark.order(32)
    @pytest.mark.regression
    @allure.description("""
    This test verifies that a user can successfully search for a task by its description, ensuring that the correct task is displayed in the search results.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC32: Successful search for a task by its description.")
    def test_task_search_by_description(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        try:
            # Steps:
            self.home_page.click_search_button()
            self.home_page.enter_search_request(task_description)
            self.home_page.is_search_results_section_contains_task(task_description)
            self.home_page.click_on_search_result(task_description)
            self.task_page.is_opened()
            self.task_page.is_task_contains_description(task_description)
        except Exception as e:
            take_screenshot(self.driver, "Task Search by Description Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @pytest.mark.order(36)
    @pytest.mark.regression
    @allure.description("""
    This test verifies that a user can successfully search for a task containing links, ensuring that tasks with URLs are correctly identified and displayed in the search results.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC36: Successful search for a task that contains links.")
    def test_task_search_by_link(self, login, delete_task):
        links = ["https://github.com/", "https://www.youtube.com/", "https://www.google.com/"]
        link = random.choice(links)
        fake = FakeDataGenerator()
        task_name = fake.task_name
        try:
            # Steps:
            self.home_page.click_add_task_button()
            self.home_page.enter_task_name(task_name + " " + link)
            self.home_page.click_submit_add_task_button()
            self.home_page.click_search_button()
            self.home_page.enter_search_request(link)
            self.home_page.press_enter()
            self.search_page.is_page_heading_contains_search_result(link)
            self.search_page.is_task_list_contains_task(task_name)
        except Exception as e:
            take_screenshot(self.driver, "Task Search by Link Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @pytest.mark.order(37)
    @pytest.mark.regression
    @allure.description("""
    This test verifies that a user can successfully search for a task with a specific comment, ensuring that tasks containing the specified comment are correctly identified and displayed in the search results.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC37: Successful search for a task with a specific comment.")
    def test_task_search_by_comment(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        fake = FakeDataGenerator()
        comment = fake.comment
        try:
            # Steps:
            self.home_page.open_task(task_name)
            self.task_page.click_comment_button()
            self.task_page.enter_comment(comment)
            self.task_page.click_add_comment_button()
            self.task_page.close_task()
            self.home_page.click_search_button()
            self.home_page.enter_search_request(comment)
            self.home_page.press_enter()
            self.search_page.click_comments_button()
            self.search_page.is_page_heading_contains_search_result(comment)
            self.search_page.is_task_list_contains_task_with_comment(task_name)
        except Exception as e:
            take_screenshot(self.driver, "Task Search by Comment Test Failed")
            raise e
        finally:
            # Postconditions:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)
