from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r'C:\Users\Mila\Desktop\meine\SM\Automation Testing\git\MilaQa'
    DRIVER_NAME = r'\chromedriver.exe'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()