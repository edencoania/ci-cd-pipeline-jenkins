"""
written - eden coania
date - 2/12/23
check - dimitri
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def startTest():
    url = 'http://127.0.0.1:1234/'
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(5)
    XPATH_city = '/html/body/form/input[1]'
    browser.find_element(By.XPATH, XPATH_city).send_keys('london')
    sleep(2)
    XPATHClick= "/html/body/form/input[2]"
    browser.find_element(By.XPATH,XPATHClick).click()
    sleep(5)
    print("good1")

    #second test
    browser.get(url)
    sleep(2)
    XPATH_city = '/html/body/form/input[1]'
    browser.find_element(By.XPATH, XPATH_city).send_keys('paris')
    sleep(2)
    XPATHClick= "/html/body/form/input[2]"
    browser.find_element(By.XPATH,XPATHClick).click()
    sleep(2)
    print("good1")


    # third test
    browser.get(url)
    sleep(2)
    XPATH_city = '/html/body/form/input[1]'
    browser.find_element(By.XPATH, XPATH_city).send_keys('tyrol')
    sleep(2)
    XPATHClick = "/html/body/form/input[2]"
    browser.find_element(By.XPATH, XPATHClick).click()
    sleep(2)
    print("good1")


    # third test
    browser.get(url)
    sleep(2)
    XPATH_city = '/html/body/form/input[1]'
    browser.find_element(By.XPATH, XPATH_city).send_keys('berlin')
    sleep(2)
    XPATHClick = "/html/body/form/input[2]"
    browser.find_element(By.XPATH, XPATHClick).click()
    sleep(2)
    print("good1")



if __name__=='__main__':
    try:
        startTest()
    except:
        print("error - try starting the web app or changing the ip address")
