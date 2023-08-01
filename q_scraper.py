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

with open('ip.txt') as f:
    datafile = f.readlines()

found = False

def check(ip):
    global found
    for line in datafile:
        if ip in line:
             found = True


def run(propro):
        # chrome_options = uc.ChromeOptions()
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--proxy-server=socks5://52.157.88.150:80')
        chrome_options.add_argument(f'--proxy-server={propro}')
        # driver = uc.Chrome(use_subprocess=True, chrome_options=chrome_options)
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=chrome_options)
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
        try:
            driver.get("https://faucet.qtestnet.org/")
            # get element
            pw = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/form/div[2]/div/div/div/div[2]")
            pw.send_keys("kopisaja")
            create = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div[1]/form/button")
            create.click()
        except WebDriverException:
            print("this ip error: "+propro)
            file_object.write("\n" + propro)
            driver.quit()
        except NoSuchElementException:
            print("this ip error: "+propro)
            file_object.write("\n" + propro)
            driver.quit()

file_object = open('ip.txt', 'a')


def mulai():
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        #driver1 = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
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
            except NoSuchElementException:
                print("this ip error: " + proxy)
                time.sleep(2)
            if column == cell[-1]:
                mulai()


mulai()
file_object.close()












#Proxy Connection

# print(colored('Getting Proxies from graber...','green'))
# time.sleep(2)
# proxy = {"http": "http://"+ column[0]+":"+column[1]}
# print(proxy)
# url = 'https://mobile.facebook.com/login'
# r = requests.get(url,  proxies=proxy)
# print("")
# print(colored('Connecting using proxy' ,'green'))
# print("")
# sts = r.status_code
# print(sts)
# proxy = column[0]+":"+column[1]
# ip = column[0]
# options = webdriver.ChromeOptions()
# #options.add_argument('headless')
# # options.add_argument(f'--proxy-server=socks5://{proxy}')
# # options.AddArgument($"--proxy-server=socks5://{proxy}");
# options.add_argument(f'--proxy-server=socks5://{ip}')
# browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), crhome_options=options)
# browser.get("https://ipsaya.com")
# #element = browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[3]/div[3]/div[1]/button[2]")
# #print(element)
