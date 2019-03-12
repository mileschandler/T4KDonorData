import time
from datetime import datetime, timedelta
from threading import Thread

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def open_page():
    URL = 'https://nfp.everydayhero.com/admin/organisations/7717ddef-6908-4b09-9c3d-498aa4b9c081/reporting/supporter-pages'
    email = 'miles.chandler@ichandler.net'
    pwd = 'risc932WEBBLAMAC$'

    browser = webdriver.Chrome('chromedriver')
    browser.get(URL)
    mouse = browser.find_element_by_id('email')
    mouse.send_keys(email)
    mouse.send_keys(Keys.ENTER)
    time.sleep(5)

    mouse = browser.find_element_by_id('sign-in-email')
    mouse.send_keys(email)
    password = browser.find_element_by_id('sign-in-password')
    password.send_keys(pwd)
    password.send_keys(Keys.ENTER)
    time.sleep(8)

    report_link = browser.find_element_by_link_text('Reporting')
    report_link.click()
    time.sleep(4)
    start_time = browser.find_element_by_id('start_time')
    now = datetime.now()
    yesterday = (now - timedelta(days=1)).strftime("%m/%d/%Y")
    today = now.strftime("%m/%d/%Y")
    start_time.send_keys(yesterday)
    end_time = browser.find_element_by_id('end_time')
    end_time.send_keys(today)

    mouse = browser.find_element_by_class_name('hui-Button__label')
    mouse.click()
    
    

    


open_page()
