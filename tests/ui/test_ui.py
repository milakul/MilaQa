import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import time

@pytest.mark.ui 
def test_check_incorrect_username():
    driver = webdriver.Chrome(
       service=Service(r'C:\Users\Mila\Desktop\meine\SM\Automation Testing\git\MilaQa' + r'\chromedriver.exe') 
    )

    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, "login_field")

    login_elem.send_keys("sergiibutenko@istakeinemail.com")

    pass_elem = driver.find_element(By.ID, "password")

    pass_elem.send_keys("wrong password")

    btn_elem = driver.find_element(By.NAME, "commit")

    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"
    #time.sleep(3)

    driver.close()