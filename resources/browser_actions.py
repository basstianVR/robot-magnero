from robot.api.deco import keyword
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .driver_manager import set_driver, get_driver

class BrowserManager:

    @keyword("Open Chrome With Manager")
    def open_browser(self, url):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get(url)
        set_driver(driver)

    @keyword("Close Browser")
    def close_browser(self):
        driver = get_driver()
        if driver:
            driver.quit()
    
    @keyword("Set Implicit Wait")
    def set_implicit_wait(self, seconds):
        driver = get_driver()
        if driver:
            driver.implicitly_wait(int(seconds))
        else:
            print("⚠️ No active driver to apply implicit wait.")
    
