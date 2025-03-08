from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Base:
    
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://practice-automation.com/form-fields"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
    
    def wait(self, time=10):
        return WebDriverWait(self.driver, time)

    def goto_site(self):
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(2)
        # открываю страницу и не дожидаюсь ее полной загрузки
        try:
            self.driver.get(self.base_url)
        except TimeoutException:
            pass