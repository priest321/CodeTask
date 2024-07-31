from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SeleniumTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.element = None
        
    def open_browser(self):
        self.driver.maximize_window()

    def navigate_to(self, url=None):
        self.driver.get(url)

    def input_text(self, search_type=None, locator="", text=""):
        search_func = None
        match search_type:
            case "name":
                search_func = By.NAME
            case "id":
                search_func = By.ID
            case "xpath":
                search_func = By.XPATH
            case "link_text":
                search_func = By.LINK_TEXT
            case "partial_link_text":
                search_func = By.PARTIAL_LINK_TEXT
            case "tag_name":
                search_func = By.TAG_NAME
            case "class_name":
                search_func = By.CLASS_NAME
            case "css_selector":
                search_func = By.CSS_SELECTOR
        
        self.element = self.driver.find_element(search_func, locator)
        self.element.clear()
        self.element.send_keys(text)

    def click_button(self, locator):
        element = self.driver.find_element(By.NAME, locator)
        element.click()

    def press_enter(self):
        self.element.send_keys(Keys.RETURN)
        
    def close_browser(self):
        self.driver.quit()


keyword = SeleniumTest()


keywords = {
    "OPEN_BROWSER": keyword.open_browser,
    "NAVIGATE_TO": keyword.navigate_to,
    "INPUT_TEXT": keyword.input_text,
    "PRESS_ENTER": keyword.press_enter,
    "CLOSE_BROWSER": keyword.close_browser,
}


test_case = [
    ("OPEN_BROWSER", {}),
    ("NAVIGATE_TO", {"url":"https://www.google.com"}),
    ("INPUT_TEXT", {"search_type": "name", "locator": "q", "text": "Python keyword driven"}),
    ("PRESS_ENTER", {}),
    ("CLOSE_BROWSER", {})
]



def execute_test_case(test_case):
    for keyword, kargs in test_case:
        if keyword in keywords:
            keywords[keyword](**kargs)
            time.sleep(1)
        else:
            print(f"Keyword {keyword} not found")


if __name__ == "__main__":
    execute_test_case(test_case)