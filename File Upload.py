import time

from selenium import webdriver
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import autoit

driver=webdriver.Firefox(executable_path="E://Software/WebDrivers/geckodriver")

driver.get("https://jpg2pdf.com/")
driver.find_element(By.XPATH,'/html/body/div/div[3]/div[2]/div[1]/span[2]').click()
time.sleep(3)

'''
#Using AutoIT
autoit.win_wait_active("[CLASS:#32770]", 3)
autoit.control_send("[CLASS:#32770]", "Edit1", "E:\Software\Pyhton-Sel\Par.jpg")
autoit.control_click("[CLASS:#32770]", "Button1")
'''

#Using Script
autoit.run("E://Software/Pyhton-Sel/Fileuploadscript.exe")
time.sleep(5)
driver.quit()