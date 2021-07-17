from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

google=driver.get("https://www.google.com/")

#google=driver.find_element_by_class_name("gLFyf gsfi") //Not allowed due to compund class

google=driver.find_element_by_xpath("//*[@name='q']")

#google=driver.find_element_by_xpath("//input[@class='gLFyf gsfi']") This code also works

google.send_keys("success")  #To pass the text on search box

#driver.get("http://demo.automationtesting.in/Windows.html")

#driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click() #To click on the object

time.sleep(3) #Used to stay on page for require time

driver.close()

