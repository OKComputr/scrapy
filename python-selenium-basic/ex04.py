from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

from time import sleep

print('Enter the gmailid and password')
gmailId = "andrea@darlingventures.com"
partOne = "@P&7"
partTwo = "%"
PartThree = "aP1988!DV" 
passWord = partOne + partTwo + PartThree

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
driver.get(r'https://darlingventures.affinity.co/auth/signin')
driver.implicitly_wait(15)

pyautogui.moveTo(687, 365, 2, pyautogui.easeInOutQuad)
pyautogui.click()

loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys(gmailId)

sleep(1.5)

nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()

sleep(1.5)

passWordBox = driver.find_element_by_xpath(
    '//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys(passWord)
sleep(1.5)

nextButton2 = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton2[0].click()

sleep(2)

driver.navigate().to('https://darlingventures.affinity.co/companies/views/206302-all-organizations')