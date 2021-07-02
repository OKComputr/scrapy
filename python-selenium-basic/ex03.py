from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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
driver.get(r'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
driver.implicitly_wait(15)

loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
loginBox.send_keys(gmailId)

sleep(3)

nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
nextButton[0].click()

sleep(3)

passWordBox = driver.find_element_by_xpath(
    '//*[@id ="password"]/div[1]/div / div[1]/input')
passWordBox.send_keys(passWord)

sleep(3)

nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
nextButton[0].click()

