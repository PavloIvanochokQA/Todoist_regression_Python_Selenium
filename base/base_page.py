import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open the page {self.PAGE_URL}."):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Verify that the page with the URL {self.PAGE_URL} is opened."):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def wait_for_visibility(self, locator, timeout=10):
        return self.wait.until(EC.visibility_of_element_located(locator), timeout)
    