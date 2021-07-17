import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

#cap = DesiredCapabilities().FIREFOX

#cap["marionette"] = False

driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("https://www.geeksforgeeks.org/")

element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT,"Courses"))
    )
print("Element located")
#EC.presence_of_element_located also can be used in line 14
# click the element
element.click()
element2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH,"//*[@class='header--nav__link login-modal-btn']"))
    )
print("Element located-2")
element2.click()
element3 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID,'luser'))
    )
print("Element located-3")
driver.quit()


