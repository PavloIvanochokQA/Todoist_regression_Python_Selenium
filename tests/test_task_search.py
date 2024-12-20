import allure
import random
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


class TestTaskSearch(BaseTest):

    @allure.feature("Task Search")
    @allure.description("""
    This test verifies that a user can successfully search for a task by its exact name, ensuring that the correct task is displayed in the search results.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC31: Successful search for a task by its name.")
    def test_task_search_by_name(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        # Steps:
        try:
            self.home_page.click_search_button()
            self.home_page.enter_search_request(task_name)
            self.home_page.is_search_results_section_contains_task(task_name)
            self.home_page.click_on_search_result(task_name)
            self.task_page.is_opened()
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Search")
    @allure.description("""
    This test verifies that a user can successfully search for a task by its description, ensuring that the correct task is displayed in the search results.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC32: Successful search for a task by its description.")
    def test_task_search_by_description(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        # Steps:
        try:
            self.home_page.click_search_button()
            self.home_page.enter_search_request(task_description)
            self.home_page.is_search_results_section_contains_task(task_description)
            self.home_page.click_on_search_result(task_description)
            self.task_page.is_opened()
            self.task_page.is_task_contains_description(task_description)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Search")
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
        # Steps:
        try:
            self.home_page.click_add_task_button()
            self.home_page.enter_task_name(task_name + " " + link)
            self.home_page.click_submit_add_task_button()
            self.home_page.click_search_button()
            self.home_page.enter_search_request(link)
            self.home_page.press_enter()
            self.search_page.is_page_heading_contains_search_result(link)
            self.search_page.is_task_list_contains_task(task_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Search")
    @allure.description("""
    This test verifies that a user can successfully search for a task with a specific comment, ensuring that tasks containing the specified comment are correctly identified and displayed in the search results.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC37: Successful search for a task with a specific comment.")
    def test_task_search_by_comment(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        fake = FakeDataGenerator()
        comment = fake.comment
        # Steps:
        try:
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
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Search")
    @allure.description("""
    This test verifies that a user can successfully search for a sub-task by its name, ensuring that the sub-task is correctly identified and displayed in the search results.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC38: Successful search for a sub-task by its name.")
    def test_subtask_search_by_name(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        fake = FakeDataGenerator()
        subtask_name = fake.task_name
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.click_add_subtask_button()
            self.task_page.enter_subtask_name(subtask_name)
            self.task_page.click_add_task_button()
            self.task_page.close_task()
            self.home_page.click_search_button()
            self.home_page.enter_search_request(subtask_name)
            self.home_page.is_search_results_section_contains_task(subtask_name)
            self.home_page.click_on_search_result(subtask_name)
            self.task_page.is_opened()
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Search")
    @allure.description("""
    This test verifies that when a user searches for non-existent information, the search results do not display any matching tasks, confirming that the system handles such cases properly.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC39: Unsuccessful search for a task with non-existent information.")
    def test_unsuccessful_task_search(self, login):
        fake = FakeDataGenerator()
        request = fake.task_name
        # Steps:
        self.home_page.click_search_button()
        self.home_page.enter_search_request(request)
        self.home_page.press_enter()
        self.search_page.is_page_heading_contains_search_result(request)
        self.search_page.is_task_list_empty(request)
        self.search_page.click_comments_button()
        self.search_page.is_task_list_empty(request)
