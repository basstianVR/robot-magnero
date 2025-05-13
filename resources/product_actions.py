from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from .driver_manager import get_driver
from .browser_actions import BrowserManager

class ProductActions:
    @keyword("Click Men Category")
    def click_men_category(self):
        driver = get_driver()
        men_button = driver.find_element(By.XPATH, "//span[normalize-space()='Men']")
        men_button.click()