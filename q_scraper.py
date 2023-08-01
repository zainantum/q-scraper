# Import Modules

from selenium import webdriver
# import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import sys
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from eth_account import Account
import secrets

with open('ip.txt') as f:
    datafile = f.readlines()

found = False
listEth = open("privatekey.txt", "a")


def check(ip):
    global found
    for line in datafile:
        if ip in line:
            found = True


def run(propro):
    # chrome_options = uc.ChromeOptions()
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=socks5://52.157.88.150:80')
    chrome_options.add_argument(f'-- proxy-server={propro}')
    # driver = uc.Chrome(use_subprocess=True, chrome_options=chrome_options)
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument("window-size=1280,800")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chrome_options)
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    try:
        driver.get("https://faucet.qtestnet.org/")
        time.sleep(4)
        priv = secrets.token_hex(32)
        private_key = "0x" + priv
        print("SAVE BUT DO NOT SHARE THIS:", private_key)
        acct = Account.from_key(private_key)
        print("Address:", acct.address)

        # get element
        pw = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/form/div[2]/div/div/div/div[2]/input[1]")
        pw.send_keys(acct.address)
        time.sleep(10)
        create = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/form/button")
        create.click()
        time.sleep(15)
        info = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/form/div[3]/p")
        if acct.address in info.text:
            print("claim dengan address sukses: " + acct.address)
            listEth.write("\n" + private_key)
            time.sleep(2)
            driver.quit()
        else:
            print("claim dengan address gagal: " + acct.address)
            time.sleep(2)
            driver.quit()
    except WebDriverException:
        print("this ip error: " + propro)
        file_object.write("\n" + propro)
        driver.quit()
    except NoSuchElementException:
        print("this ip error: " + propro)
        file_object.write("\n" + propro)
        driver.quit()


file_object = open('ip.txt', 'a')


def mulai():
    i = 0
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    # driver1 = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
    driver1 = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    driver1.get("https://www.sslproxies.org/")
    tbody = driver1.find_element_by_tag_name("tbody")
    cell = tbody.find_elements_by_tag_name("tr")
    for column in cell:
        # print(column.text)
        column = column.text.split(" ")
        proxy = column[0] + ":" + column[1]
        print(proxy)
        try:
            run(proxy)
            i += 1
        except NoSuchElementException:
            print("this ip error: " + proxy)
            i += 1
            time.sleep(2)
        if column == cell[-1]:
            mulai()


mulai()
file_object.close()
listEth.close()
