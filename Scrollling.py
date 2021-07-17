from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver")


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#Scroll By Pixel
driver.execute_script("window.scrollBy(0,1000)","")

#Scroll down till the element is visible
#flag=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

#Scroll till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

