import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By

from ReadExcel import rows

driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver.exe")

driver.get("https://the-internet.herokuapp.com/login")

path="E:\Software\Pyhton-Sel\login.xlsx"

rows=XLUtils.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    username=XLUtils.readData(path,'Sheet1',r,1)
    password=XLUtils.readData(path,'Sheet1',r,2)
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/button/i').click()

if driver.find_element(By.XPATH, '/html/body/div[2]/div/div/a').is_displayed():
    print("Test Pass")
    XLUtils.writeData(path, "Sheet1", r, 3, "Login pass")
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/a').click()
else:
    print("Test Fail")
    XLUtils.writeData(path,"Sheet1",r,3,"Login Fail")
'''   
try:
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div/a').click()
except:
    print("Test Fail")
    XLUtils.writeData(path, "Sheet1", r, 3, "Login fail")
else:
    print("Test Pass")
    XLUtils.writeData(path, "Sheet1", r, 3, "Login pass")
'''