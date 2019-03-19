from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def base_find_element(self, timeout=30, poll=0.5):
        WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until()