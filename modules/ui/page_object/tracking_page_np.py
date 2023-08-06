from modules.ui.page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class TrackingPage(BasePage):
    URL = 'https://tracking.novaposhta.ua/#/uk/'

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(TrackingPage.URL)

   

    def search_cargo(self, number):
        tracking_elem = self.driver.find_element(By.ID, "en")

        tracking_elem.send_keys(number)


        btn_elem = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")

        btn_elem.click()



#Протестувати з Головної так і не вдалося. Після різних експериментів з локатороми, спроби приховати попап при відкритті сторінки - зафейлилися.
#Аналогічно і з кнопкою у формі відправки номера накладної (на головній нової пошти)

# class TrackingMainPage(BasePage):
#     URL = 'https://novaposhta.ua/'

#     def __init__(self) -> None:
#         super().__init__()
    
#     def go_to(self):
#         self.driver.get(TrackingMainPage.URL)

#     # def close_popup(self):
#     #     close_elem = self.driver.find_element(By...., "....") 
#     #     close_elem.click()


#     def search_cargo(self, number):
#         tracking_elem = self.driver.find_element(By.ID, "cargo_number")

#         tracking_elem.send_keys(number)

#         btn_elem = self.driver.find_element(By.XPATH, "//*[@id='top_block']/div[1]/div/div[2]/form/input[2]")

#         btn_elem.click()





 