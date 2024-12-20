import allure
import random
from base.base_test import BaseTest
from utils.fake_data_generator import FakeDataGenerator


class TestTaskManagement(BaseTest):

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a task can be successfully created with all required fields filled.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC12: Successful task creation.")
    def test_task_creation(self, login, delete_task):
        fake = FakeDataGenerator()
        task_name = fake.task_name
        task_description = fake.task_description
        task_priority = random.randint(1, 4)
        # Steps:
        try:
            self.home_page.click_add_task_button()
            self.home_page.enter_task_name(task_name)
            self.home_page.enter_description(task_description)
            self.home_page.set_task_priority(task_priority)
            self.home_page.click_submit_add_task_button()
            self.home_page.is_task_list_contains_task(task_name)
            self.home_page.open_task(task_name)
            self.task_page.is_opened()
            self.task_page.is_task_contains_description(task_description)
            self.task_page.is_task_has_priority(task_priority)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that the name, description, and priority of a task can be successfully updated.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC13: Successful change of name, description, and priority for a task.")
    def test_task_editing(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        fake = FakeDataGenerator()
        new_task_name = fake.task_name
        new_task_description = fake.task_description
        new_task_priority = random.randint(1, 4)
        is_task_name_changed = False
        # Steps:
        try:
            self.home_page.click_edit_button(task_name)
            self.home_page.enter_task_name(new_task_name)
            self.home_page.enter_description(new_task_description)
            self.home_page.set_task_priority(new_task_priority)
            self.home_page.click_save_button()
            self.home_page.is_task_list_contains_task(new_task_name)
            is_task_name_changed = True
            self.home_page.open_task(new_task_name)
            self.task_page.is_opened()
            self.task_page.is_task_contains_description(new_task_description)
            self.task_page.is_task_has_priority(new_task_priority)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                task_name_to_use = new_task_name if is_task_name_changed else task_name
                delete_task(task_name_to_use)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a sub-task can be successfully added to an existing task.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC14: Successful addition of a sub-task.")
    def test_subtask_creation(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        fake = FakeDataGenerator()
        subtask_name = fake.task_name
        subtask_description = fake.task_description
        subtask_priority = random.randint(1, 4)
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.is_opened()
            self.task_page.click_add_subtask_button()
            self.task_page.enter_subtask_name(subtask_name)
            self.task_page.enter_subtask_description(subtask_description)
            self.task_page.set_subtask_priority(subtask_priority)
            self.task_page.click_add_task_button()
            self.task_page.is_subtask_list_contains_subtask(subtask_name)
            self.task_page.open_subtask(subtask_name)
            self.task_page.is_task_contains_description(subtask_description)
            self.task_page.is_task_has_priority(subtask_priority)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task"):
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that the due date and time of an existing task can be successfully updated.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC15: Successful change of task due date and time.")
    def test_due_date_and_time_update(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        random_time = f"{hour:02d}:{minute:02d}"
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.is_opened()
            self.task_page.click_due_date_button()
            self.task_page.click_time_button()
            self.task_page.enter_time(random_time)
            self.task_page.click_save_button()
            self.task_page.click_tomorrow_button()
            self.task_page.is_task_contains_due_date(f"Tomorrow {random_time}")
            self.task_page.click_due_date_button()
            self.task_page.click_today_button()
            self.task_page.is_task_contains_due_date(f"Today {random_time}")
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a task can be successfully marked as completed and moved to the \"Completed\" section.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC16: Successful task completion and marking as completed.")
    def test_mark_task_as_completed(self, login, create_task):
        task_name, task_description, task_priority = create_task
        # Steps:
        self.home_page.click_checkbox_on_task(task_name)
        self.home_page.is_task_list_not_contains_task(task_name)
        self.home_page.open_completed_section()
        self.home_page.is_completed_section_contains_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a task can be successfully deleted and is no longer visible in the task list.
    """)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("TC17: Successful task deletion.")
    def test_task_deletion(self, login, create_task):
        task_name, task_description, task_priority = create_task
        # Steps:
        self.home_page.click_more_actions_button(task_name)
        self.home_page.click_delete_button()
        self.home_page.confirm_deletion()
        self.home_page.is_task_list_not_contains_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a task can be successfully created with a link, and clicking the link opens a new browser tab with the correct URL.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC18: Successful task creation with a link.")
    def test_task_creation_with_link(self, login, delete_task):
        links = ["https://github.com/", "https://www.youtube.com/", "https://www.google.com/"]
        link = random.choice(links)
        fake = FakeDataGenerator()
        task_name = fake.task_name
        # Steps:
        try:
            self.home_page.click_add_task_button()
            self.home_page.enter_task_name(task_name + " " + link)
            self.home_page.click_submit_add_task_button()
            self.home_page.click_link_in_task(task_name)
            self.home_page.is_link_opened(link)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""This test verifies that a user can successfully add a comment to a task and that the comment appears in the "Comments" section.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC19: Successful addition of a comment to a task.")
    def test_add_comment(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        fake = FakeDataGenerator()
        comment = fake.comment
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.is_opened()
            self.task_page.click_comment_button()
            self.task_page.enter_comment(comment)
            self.task_page.click_add_comment_button()
            self.task_page.is_comments_section_contains_comment(comment)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a user can successfully add a label to a task.
    It ensures that the label is visible in the task's details and can be used to filter tasks.
    """)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("TC20: Successful addition of a label to a task.")
    def test_add_label(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        labels = ["Education", "Sport", "Personal", "Work", "Hobby"]
        label = random.choice(labels)
        # Steps:
        try:
            self.home_page.open_task(task_name)
            self.task_page.is_opened()
            self.task_page.click_labels_button()
            self.task_page.set_label(label)
            self.task_page.click_on_label(label)
            self.home_page.is_page_heading_contains_label(label)
            self.home_page.is_task_list_contains_task(task_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task."):
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a user can successfully duplicate a task.
    It ensures that the duplicated task has the same details as the original task and appears in the task list.
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC21: Successful task duplication.")
    def test_task_duplication(self, login, create_task, delete_task):
        task_name, task_description, task_priority = create_task
        # Steps:
        try:
            self.home_page.click_more_actions_button(task_name)
            self.home_page.click_duplicate_button()
            self.home_page.is_task_list_contains_duplicate(task_name)
        # Postconditions:
        finally:
            with allure.step("Postconditions: Delete the created task and its duplicate."):
                delete_task(task_name)
                delete_task(task_name)

    @allure.feature("Task Management")
    @allure.description("""
    This test verifies that a user cannot create a task with invalid information (when the task name is missing).
    """)
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("TC22: Unsuccessful task creation with invalid information.")
    def test_unsuccessful_task_creation(self, login):
        fake = FakeDataGenerator()
        task_name = ""
        task_description = fake.task_description
        task_priority = random.randint(1, 4)
        # Steps:
        self.home_page.click_add_task_button()
        self.home_page.enter_task_name(task_name)
        self.home_page.enter_description(task_description)
        self.home_page.set_task_priority(task_priority)
        self.home_page.is_add_task_button_disabled()
