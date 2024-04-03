
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://10.10.32.1:2280/cportal")
driver.maximize_window();
driver.switch_to.frame("login_win")

username = "21ec128" 
password = "123456"

usrid = "usrname"
passid = "newpasswd"
submit = "update_btn"
driver.find_element(By.ID, usrid).send_keys(username)
driver.find_element(By.ID, passid).send_keys(password)
time.sleep(2)
driver.find_element(By.ID, submit).submit()
time.sleep(2)
driver.quit()