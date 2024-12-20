import allure
import random
from base.base_test import BaseTest


class TestTaskFiltering(BaseTest):

    @allure.feature("Task Filtering")
    @allure.description("""
    This test verifies that a user can successfully filter tasks by their priority, ensuring the filtered tasks match the specified priority and display correctly in the task list.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC33: Successful filtering for a task by its priority.")
    def test_task_filtering_by_priority(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        priority = f"Priority {task_priority}"
        # Steps:
        try:
            self.home_page.click_search_button()
            self.home_page.enter_search_request(priority)
            self.home_page.press_enter()
            self.search_page.is_opened()
            self.search_page.is_page_heading_contains_search_result(priority)
            self.search_page.is_task_list_contains_task(task_name)
            self.search_page.open_task(task_name)
            self.task_page.is_opened()
            self.task_page.is_task_has_priority(task_priority)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Filtering")
    @allure.description("""
    This test verifies that a user can successfully filter tasks by their label, ensuring the filtered tasks match the specified label and display correctly in the task list.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC34: Successful filtering for a task by its label.")
    def test_task_filtering_by_label(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        labels = ["Education", "Sport", "Personal", "Work", "Hobby"]
        label = random.choice(labels)
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.click_labels_button()
            self.task_page.set_label(label)
            self.task_page.close_task()
            self.home_page.click_search_button()
            self.home_page.enter_search_request(label)
            self.home_page.click_on_search_result(label)
            self.search_page.is_page_heading_contains_label(label)
            self.search_page.is_task_list_contains_task(task_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Filtering")
    @allure.description("""
    This test verifies that a user can successfully filter tasks by their due date, ensuring the filtered tasks match the specified date and display correctly in the task list.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC35: Successful filtering for a task by its due date.")
    def test_task_filtering_by_due_date(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        due_date = "Tomorrow"
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.click_due_date_button()
            self.task_page.click_tomorrow_button()
            self.task_page.close_task()
            self.home_page.click_search_button()
            self.home_page.enter_search_request(due_date)
            self.home_page.press_enter()
            self.search_page.is_page_heading_contains_search_result(due_date)
            self.search_page.is_task_list_contains_task(task_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                self.home_page.open_task(task_name)
                self.task_page.click_due_date_button()
                self.task_page.click_today_button()
                delete_task(task_name)
