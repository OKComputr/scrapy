from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
browser.get('https://signal.nfx.com/investor-lists/top-marketingtech-seed-investors')


while True:
    # grab the data

    # click next link
    try:
        loadMore = browser.find_element_by_xpath("//button[@class='btn-xs sn-light-greyblue-accent-button sn-center mt3 mb2 btn btn-default'][.='LOAD MORE INVESTORS']")
        loadMore.click()
        sleep(3)
    except TimeoutException:
        break