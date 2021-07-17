import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("http://testautomationpractice.blogspot.com/")

Alert=driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button")

Alert.click()

time.sleep(3)

driver.switch_to.alert.accept() #To click ok,accept

Alert.click()

driver.switch_to.alert.dismiss() #To click cancel

driver.close()





