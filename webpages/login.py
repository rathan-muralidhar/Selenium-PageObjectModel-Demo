#Webpage accessed: https://demoqa.com/login
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config.configs import login_url

class LoginPage:
    _username_we = {"by": By.ID, "value": "userName"}
    _password_we = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.ID, "value": "login"}

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(login_url)

    def using(self, username, password):
        self.driver.find_element(self._username_we["by"],
                                 self._username_we["value"]).send_keys(username)
        self.driver.find_element(self._password_we["by"],
                                 self._password_we["value"]).send_keys(password)
        self.driver.execute_script("window.scrollBy(0,300)","")
        self.driver.find_element(self._submit_button["by"],
                                 self._submit_button["value"]).click()
        try:
            WebDriverWait(self.driver,timeout=3).until(EC.url_contains("profile"))
        except:
            pass

    def get_url(self):
        return self.driver.current_url