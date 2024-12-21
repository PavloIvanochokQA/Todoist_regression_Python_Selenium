import allure
from selenium.webdriver.remote.webdriver import WebDriver


def take_screenshot(driver: WebDriver, name="Screenshot"):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
