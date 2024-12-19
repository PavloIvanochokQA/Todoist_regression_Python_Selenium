import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TaskPage(BasePage):

    PAGE_URL = Links.TASK_PAGE

    PRIORITY_DROPDOWN = ("xpath", "(//button[@aria-haspopup='listbox'])[2]")
    DESCRIPTION_VALUE = ("xpath", "//div[@class='task_content']/p")
    ADD_SUBTASK_BUTTON = ("xpath", "//button[@class='fb8d74bb _56a651f6 _3930afa0 aa19cb97 _1e29d236']")
    SUBTASK_NAME_FIELD = ("xpath", "//p[@data-placeholder='Task name']")
    SUBTASK_DESCRIPTION_FIELD = ("xpath", "//p[@data-placeholder='Description']")
    SUBTASK_PRIORITY_DROPDOWN = ("xpath", "//div[@aria-label='Set priority']")
    ADD_TASK_BUTTON = ("xpath", "//button[@type='submit']")
    CANCEL_BUTTON = ("xpath", "//button[@aria-label='Cancel']")
    DUE_DATE_BUTTON = ("xpath", "//div[@class='XBdYwsn fb8d74bb ae9d1115 _96003c07']")
    DUE_DATE_VALUE = ("xpath", "//div[@class='XBdYwsn fb8d74bb ae9d1115 _96003c07']//span")
    TODAY_BUTTON = ("xpath", "//div[text()='Today']")
    TOMORROW_BUTTON = ("xpath", "//div[text()='Tomorrow']")
    NEXT_WEEK_BUTTON = ("xpath", "//div[text()='Next week']")
    TIME_BUTTON = ("xpath", "//div[@class='fb8d74bb _14423c92 e4e217d4 _2d7320f2']")
    TIME_FIELD = ("xpath", "//input[@aria-label='Start time']")
    SAVE_TIME_BUTTON = ("xpath", "//button[@type='submit']")
    CLOSE_TASK_BUTTON = ("xpath", "//button[@aria-label='Close task']")
    COMMENT_BUTTON = ("xpath", "//button[@data-testid='open-comment-editor-button']")
    COMMENT_FIELD = ("xpath", "//div[@aria-label='Comment']/p")
    ADD_COMMENT_BUTTON = ("xpath", "//button[@data-track='comments|add_comment']")
    COMMENTS_CONTAINER = ("xpath", "//div[@data-testid='comments-list-container']")
    LABELS_BUTTON = ("xpath", "(//div[@data-testid='task-details-sidebar']//button)[5]")
    LABEL_FIELD = ("xpath", "//input[@aria-label='Type a label']")

    def is_opened(self):
        with allure.step(f"Verify that the page with a URL starting with {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_contains(self.PAGE_URL))

    @allure.step("Verify that the task contains the description.")
    def is_task_contains_description(self, task_description):
        description_text = self.wait_for_visibility(self.DESCRIPTION_VALUE).text
        assert description_text == task_description, \
            f"Expected: \"{task_description}\", but got: \"{description_text}\"."

    @allure.step("Verify that the task has the assigned priority.")
    def is_task_has_priority(self, priority):
        item_locator = ("xpath", f"//li[@aria-label='Priority {priority}']")
        self.click_element(self.PRIORITY_DROPDOWN)
        item_element = self.wait_for_visibility(item_locator)
        assert item_element.get_attribute('aria-selected') == 'true', \
            f"The task does not have the assigned priority."

    @allure.step("Click on the \"Add sub-task\" button.")
    def click_add_subtask_button(self):
        self.click_element(self.ADD_SUBTASK_BUTTON)

    @allure.step("Enter sub-task name into the \"Task name\" field.")
    def enter_subtask_name(self, subtask_name):
        self.enter_text(self.SUBTASK_NAME_FIELD, subtask_name)

    @allure.step("Enter sub-task description into the \"Description\" field.")
    def enter_subtask_description(self, subtask_description):
        self.enter_text(self.SUBTASK_DESCRIPTION_FIELD, subtask_description)

    @allure.step("Set the sub-task's Priority")
    def set_subtask_priority(self, priority):
        item_locator = ("xpath", f"//ul[@aria-label='Select a priority']/li[{priority}]")
        self.click_element(self.SUBTASK_PRIORITY_DROPDOWN)
        self.click_element(item_locator)

    @allure.step("Click on the \"Add task\" button.")
    def click_add_task_button(self):
        self.click_element(self.ADD_TASK_BUTTON)
        self.click_element(self.CANCEL_BUTTON)

    @allure.step("Verify that the sub-task list contains the sub-task.")
    def is_subtask_list_contains_subtask(self, subtask_name):
        subtask_locator = (
            "xpath", f"//div[@data-testid='task-main-content-container']//div[text()='{subtask_name}']")
        try:
            self.wait_for_visibility(subtask_locator)
        except:
            raise TimeoutException(
                f"The sub-task with name \"{subtask_name}\" was not found in the sub-task list.")

    @allure.step("Open the sub-task.")
    def open_subtask(self, subtask_name):
        subtask_locator = ("xpath", f"//div[text()='{subtask_name}']")
        self.wait_for_visibility(subtask_locator)
        self.click_element(subtask_locator)

    @allure.step("Click on the \"Due date\" button.")
    def click_due_date_button(self):
        self.click_element(self.DUE_DATE_BUTTON)

    @allure.step("Click on the \"Today\" button.")
    def click_today_button(self):
        self.click_element(self.TODAY_BUTTON)

    @allure.step("Click on the \"Tomorrow\" button.")
    def click_tomorrow_button(self):
        self.click_element(self.TOMORROW_BUTTON)

    @allure.step("Click on the \"Next week\" button")
    def click_next_week_button(self):
        self.click_element(self.NEXT_WEEK_BUTTON)

    @allure.step("Click on the \"Time\" button.")
    def click_time_button(self):
        self.click_element(self.TIME_BUTTON)

    @allure.step("Enter the time into the \"Time\" field.")
    def enter_time(self, value):
        self.wait_for_visibility(self.TIME_FIELD).send_keys(Keys.DELETE)
        self.enter_text(self.TIME_FIELD, value)

    @allure.step("Click on the \"Save\" button.")
    def click_save_button(self):
        self.click_element(self.SAVE_TIME_BUTTON)

    @allure.step("Verify that the task displays the correct due date and time.")
    def is_task_contains_due_date(self, due_date):
        value_text = self.wait_for_visibility(self.DUE_DATE_VALUE).text
        assert value_text == due_date, \
            f"Due date mismatch: expected \"{due_date}\", but found \"{value_text}\" in the task."

    @allure.step("Click on the \"Close task\" button.")
    def close_task(self):
        self.click_element(self.CLOSE_TASK_BUTTON)

    @allure.step("Click on the \"Comment\" button.")
    def click_comment_button(self):
        self.click_element(self.COMMENT_BUTTON)

    @allure.step("Enter a comment into the \"Comment\" field.")
    def enter_comment(self, comment):
        self.enter_text(self.COMMENT_FIELD, comment)

    @allure.step("Click on the add \"Comment\" button.")
    def click_add_comment_button(self):
        self.click_element(self.ADD_COMMENT_BUTTON)

    @allure.step("Verify that the comment appears in the \"Comments\" section.")
    def is_comments_section_contains_comment(self, comment):
        comment_locator = ("xpath", f"//p[text()='{comment}']")
        try:
            self.wait_for_visibility(comment_locator)
        except:
            raise TimeoutException(f"Comment \"{comment}\" not found.")

    @allure.step("Click on the \"Labels\" button.")
    def click_labels_button(self):
        self.click_element(self.LABELS_BUTTON)

    @allure.step("Set a label.")
    def set_label(self, label):
        label_field = self.wait_for_visibility(self.LABEL_FIELD)
        label_field.send_keys(label)
        label_field.send_keys(Keys.ENTER)
        label_field.send_keys(Keys.ESCAPE)

    @allure.step("Click on the added label.")
    def click_on_label(self, label):
        label_locator = ("xpath", f"//a[@data-item-label-name='{label}']")
        self.click_element(label_locator)
