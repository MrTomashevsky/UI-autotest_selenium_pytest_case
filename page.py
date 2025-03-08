from base import Base
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Page(Base):
    
    # редактирование поля Name 
    def setName(self, what):
        name_input = self.driver.find_element(By.ID, "name-input")
        name_input.send_keys(what)
    
    # редактирование поля Password 
    def setPassword(self, what):
        password = self.driver.find_element(By.CSS_SELECTOR, "[type=\"password\"]")
        password.send_keys(what)

    # выбор напитка
    def selectDrink(self, what):
        drink = self.driver.find_element(By.XPATH, f"//form[@id=\"feedbackForm\"]/label[text()=\"{what}\"]")
        drink.click()
    
    # выбор цвета
    def selectColor(self, what):
        st = {
            "Red": "color1",
            "Blue": "color2",
            "Yellow": "color3",
            "Green": "color4",
            "#FFC0CB": "color5"
        }
        self.driver.execute_script(f"document.getElementById('{st[what]}').checked = true")

    # проскроллить страничку к списку "Do you like automation?"
    def scrollToAutomation(self):
        automation = self.driver.find_element(By.XPATH, "//select[@name=\"automation\"]")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", automation)
    
        # дождаться, пока проскроллиться
        pos = automation.location['y']
        while True:
            time.sleep(0.5)
            tmp_pos = automation.location['y']
            if pos == tmp_pos:
                break
            pos = tmp_pos
    
    # выбор элемента списка "Do you like automation?"
    def selectAutomation(self, what):
        automation = self.driver.find_element(By.XPATH, "//select[@name=\"automation\"]")
        do_you_like = Select(automation)
        do_you_like.select_by_value(what)

    # редактирование Email
    def setEmail(self, what):
        email = self.driver.find_element(By.ID, "email")
        email.send_keys(what)

    # редактирование Message
    # пишу в Message количество элементов списка "Automation tools" и самый длинный элемент этого же списка
    def setMessage(self):
        options = self.driver.find_element(By.CSS_SELECTOR, "#feedbackForm ul").find_elements(By.TAG_NAME, "li")
        s = str(len(options)) + " " + str(max(options, key=lambda obj: len(obj.text)).text)
        message = self.driver.find_element(By.ID, "message")
        message.send_keys(s)

    # нажатие на кнопку
    def clickButton(self):
        submit_btn = self.driver.find_element(By.ID, "submit-btn")
        submit_btn.click()

    # проверка, что появилась надпись "Message received!"
    def checkMessageAlert(self):
        self.wait(5).until(EC.alert_is_present())
        assert self.driver.switch_to.alert.text == "Message received!"
        self.driver.switch_to.alert.accept()