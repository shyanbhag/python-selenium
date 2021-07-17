import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver=webdriver.Firefox(executable_path="E:\Software\WebDrivers\geckodriver")
'''
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID,"txtUsername").send_keys("admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()

admin=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b")
usermng=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
            users=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

time.sleep(3)

#Below two line code added when we get MoveTargetOutOfBoundsException
driver.execute_script("return document.body.scrollHeight")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermng).move_to_element(users).click().perform()

#Double Click
driver.get("http://testautomationpractice.blogspot.com/")

element=driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/button')

actions=ActionChains(driver)
actions.double_click(element).perform()

#Right Click
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
button=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')

ActionChains(driver).context_click(button).perform()
'''
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
source=driver.find_element(By.XPATH,'//*[@id="box6"]')
target=driver.find_element(By.XPATH,'//*[@id="box106"]')

ActionChains(driver).drag_and_drop(source,target).perform()

driver.quit()