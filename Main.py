# from selenium import webdriver
# bot = webdriver.Chrome(executable_path='chromedriver.exe')
# bot.get('https://Eshikhon.com')


import os
import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv("Eshikhon_User"))

class Eshikhonbot:
    def __init__(self):
        driver_path = os.path.join(os.getcwd(), "chromedriver.exe")
        self.bot = webdriver.Chrome(executable_path=driver_path)

    def login(self, username, password):
        K = self.bot
        K.get("https://www.eshikhon.com/wp-login.php")
        time.sleep(3)
        username_filed = K.find_element(By.NAME, "log")
        username_filed.send_keys(username)
        # username_filed.send_keys(Keys.RETURN) NO NEED THIS※
        time.sleep(3)
        Password_filed = K.find_element(By.NAME, "pwd")
        Password_filed.send_keys(password)
        Password_filed.send_keys(Keys.RETURN)
        time.sleep(5)
        click_field = K.find_element(By.XPATH, '//*[@id="course-list"]/li/div/div[2]/div/div[4]/form/input[1]')
        click_field.click()
        time.sleep(5)
        K.get('https://drive.google.com/drive/folders/1auFq1LuQbZpFN4mazl6lD3PkXDIVMFIh')
        time.sleep(10)
        list_view = K.find_element(By.XPATH, '//*[@id=":0"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[4]/div/div/div/div[1]/div[2]')
        list_view.click()
        # time.sleep(10)
        # download = K.find_element(By.XPATH, '//*[@id=":2h"]/div/c-wiz/div[2]/c-wiz/div[1]/c-wiz/div/c-wiz/div[1]/c-wiz/c-wiz/div/c-wiz[4]/div/div/div/div[6]/div/span')
        # download.click()
        time.sleep(10)
        last_work = K.find_element(By.XPATH, '/html/body/div[13]/div[3]/button[2]')
        last_work.click()
        time.sleep(10000)       
        
        
        
         # class_field = K.find_element(By.XPATH, '//*[@id="unit4052598"]/a')
        # class_field.click()
        # time.sleep(3)
        # vdo_field = K.find_element(By.ID, "button5886")
        # vdo_field.click()
        # time.sleep(100)



def main():
    Eshikhon = Eshikhonbot()
    Eshikhon.login(os.getenv("Eshikhon_User"), os.getenv("Eshikhon_Password"))

if __name__ == '__main__':
    main()

input()