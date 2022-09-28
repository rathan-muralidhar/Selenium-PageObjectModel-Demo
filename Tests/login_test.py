import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config.configs import chromedriver_location,dashboard_url,username,password,headless
from webpages.login import LoginPage

@pytest.fixture
def login():
    parent_path = os.path.dirname(os.getcwd())
    os.chdir(parent_path)
    service_object = Service(chromedriver_location)
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service_object,
                              options=chrome_options)
    login_object = LoginPage(driver)
    return login_object

def test_valid_credentials(login):
    login.using(username,password)
    assert login.get_url() == dashboard_url