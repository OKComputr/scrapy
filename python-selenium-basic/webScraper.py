
# import the webdriver
from typing import Sized
from selenium import webdriver
from selenium.webdriver.common import keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from random import randint
from random import random


import unittest
import csv

options = Options()
options.add_argument('start-maximized')
options.add_argument('disable-infobars')

urlAll = [

        'https://signal.nfx.com/investor-lists/top-gig-economy-seed-investors',
        'https://signal.nfx.com/investor-lists/top-wellness-fitness-seed-investors',
        'https://signal.nfx.com/investor-lists/top-digital-health-series-a-investors'   
]

listLength = len(urlAll)

for k in range (0,listLength):

    url = urlAll[k]

    fileName = url.rsplit('/', 1)[-1]

    browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
    browser.get(url)


    while True:
        # grab the data

        # click next link
        try:
            loadMore = browser.find_element_by_xpath("//button[@class='btn-xs sn-light-greyblue-accent-button sn-center mt3 mb2 btn btn-default'][.='LOAD MORE INVESTORS']")
            pyautogui.moveTo(randint(400,650), randint(300,1000), random()*0.3, pyautogui.easeInOutQuad)
            actions = ActionChains(browser)
            actions.move_to_element(loadMore).perform()
            loadMore.click()
            sleep(random()+1)
        except NoSuchElementException:
            break


    col = []
    col2 = []
    rows = []

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
        new = i.text
        col.append(new)
        # to get the header with text method
    rows.append(col)

    for i in range (2, rc +1) :
        temp = []
        # to traverse through the table column 
        for j in range (1, cc+1) :
        # to get all the cell data with text method
            
            try:
                sleep(0.1)
                expandInvestors = browser.find_element_by_xpath("//*[@id='sn-react-controlled-content']/div/div/main/div[1]/div[1]/div[2]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]/div/div/span")
                pyautogui.moveTo(randint(400,650), randint(300,1000), random()*0.1, pyautogui.easeInOutQuad)
                actions = ActionChains(browser)
                actions.move_to_element(expandInvestors).perform()
                expandInvestors.click()
                sleep(random()*0.1)
            except NoSuchElementException:
                pass
            d = browser.find_element_by_xpath ("//tr["+str(i)+"]/td["+str(j)+"]").text
            """ checks
            print(i)
            print(j)
            print(d)"""
            temp.append(d) 
        """print(temp)"""
        rows.append(temp)
        """print(col2)
    print(col2)"""    

        myData = rows
        myFile = open("csv-export-"+str(fileName)+".csv", 'w')
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(myData)

    sleep(2)
    # to close the browser
    browser.quit ()


    
    
"""
print(rows)
# to close the browser
browser.quit ()"""

