driver = None  # Global variable to hold the browser instance

def set_driver(instance):
    global driver
    driver = instance

def get_driver():
    return driver