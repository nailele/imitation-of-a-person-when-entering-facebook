
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time

driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get("https://www.facebook.com/")

users_login = 'username'
users_password = 'password'

users_login_1 = []
users_password_1 = []

for i in users_login:
    users_login_1.append(i)
for i in users_password:
    users_password_1.append(i)

input_time = random.randrange(1,10)
input_time = input_time * 0.1

def input_login():
    for i in users_login_1:
        login = driver.find_element_by_name('email')
        login.send_keys(i)
        time.sleep(input_time)

def input_password():
    for i in users_password_1:
        password = driver.find_element_by_name('pass')
        password.send_keys(i)
        time.sleep(input_time)



input_login()
time.sleep(input_time)
input_password()
time.sleep(input_time)
login_button = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(input_time)
driver.close()
