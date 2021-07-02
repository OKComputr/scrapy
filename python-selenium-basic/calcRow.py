
# import the webdriver
from typing import Sized
from selenium import webdriver
from selenium.webdriver.common import keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://signal.nfx.com/investor-lists/top-autotech-seed-investors')

loadMore = browser.find_element_by_xpath("//button[@class='btn-xs sn-light-greyblue-accent-button sn-center mt3 mb2 btn btn-default'][.='LOAD MORE INVESTORS']")


try:
    loadMore.click()
    sleep(1)
except NoSuchElementException:
    pass
sleep(3)
# to identify the table rows
r = browser.find_elements_by_xpath('//*[@id="sn-react-controlled-content"]/div/div/main/div[1]/div[1]/div[2]/table/tbody/tr')
# to identify table columns
c = browser.find_elements_by_xpath('//*[@id="sn-react-controlled-content"]/div/div/main/div[1]/div[1]/div[2]/table/tbody/tr[3]/td')
# to get row count with len method
rc = len (r)
# to get column count with len method
cc = len (c)
# to traverse through the table rows excluding headers
n = browser.find_elements_by_xpath('//*[@id="sn-react-controlled-content"]/div/div/main/div[1]/div[1]/div[2]/table/thead/tr[1]/th')
for i in n :
    # to get the header with text method
    print (i.text)

for i in range (2, rc + 1) :
# to traverse through the table column 
    for j in range (1, cc + 1) :
# to get all the cell data with text method
        d = browser.find_element_by_xpath ("//tr["+str(i)+"]/td["+str(j)+"]").text
        print (d)

sleep(2)
# to close the browser
browser.quit ()




