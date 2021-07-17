from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX

cap["marionette"] = False

driver=webdriver.Firefox(capabilities=cap, executable_path="E:\Software\WebDrivers\geckodriver")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()

print(driver.current_window_handle) #Returns current window value

handles=driver.window_handles #Capture all windows

#Print all windows title
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()