# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:59:14 2022

@author: Tyagi
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import glob
import time
import numpy as np
import os
from selenium.webdriver.support.ui import Select
#sources = np.loadtxt("spitzer_list.txt", dtype='str', delimiter = '#')

#%%
sources = ["hops 68", "iras 13036-7644", "[EES2009] per-emb 47"]
#driver = webdriver.Chrome(executable_path= r"C:/Users/Tyagi/OneDrive/Documents/TIFR/sed_web_scrapping/chromedriver")

ra_inp= ["16h 28m 22.22s"]
de_inp= ["-24d 36' 31.2"]

#%%
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Tyagi\Downloads\Selenium_downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})
driver = webdriver.Chrome(executable_path= r"C:/Users/Tyagi/OneDrive/Notes/chromedriver/chromedriver.exe",
                          options=options)



driver.get("http://www.ncra.tifr.res.in:8081/~secr-ops/etc/rms/rms.html")
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
#driver.maximize_window()
time.sleep(3)

def band5(ra_input, dec_input):

    search_source = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[4]/select")
    
    select = Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/select'))
    
    # select by visible text
    select.select_by_visible_text("Band-5 (980-1500 MHz)")
    
    
    ra = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[4]/input[1]")
     
    # Sending input text to search field
    action = ActionChains(driver)
        
    action.double_click(ra)
    for i in range(3):
        action.move_to_element(ra).click()
    action.perform()
    
    ra.send_keys(ra_input)
    #driver.execute_script(f"arguments[0].innerText = {ra_inp[0]}", ra)
    
    
    dec = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[4]/input[2]")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(dec)
    for i in range(3):
        action.move_to_element(dec).click()
    action.perform()
    dec.send_keys(dec_input)
    #driver.execute_script(f"arguments[0].innerText = {de_inp[0]}", dec)
    
    
    rms = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[15]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(rms)
    for i in range(3):
        action.move_to_element(rms).click()
    action.perform()
    rms.send_keys(10)
    
    fudge = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[19]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(fudge)
    for i in range(3):
        action.move_to_element(fudge).click()
    action.perform()
    fudge.send_keys(3)
    
    polarization = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[22]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(polarization)
    for i in range(3):
        action.move_to_element(polarization).click()
    action.perform()
    polarization.send_keys("00h 00m 00s")
    
    calculate = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[26]/td/input[1]")
    calculate.click()
    
    time.sleep(3)
    
    
    download_pdf = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[26]/td/input[3]")
    download_pdf.click()
    
def band4(ra_input, dec_input):
    


    search_source = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[4]/select")
    
    select = Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/select'))
    
    # select by visible text
    select.select_by_visible_text("Band-4 (550-850 MHz)")
    
    
    ra = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[4]/input[1]")
     
    # Sending input text to search field
    action = ActionChains(driver)
        
    action.double_click(ra)
    for i in range(3):
        action.move_to_element(ra).click()
    action.perform()
    
    ra.send_keys(ra_input)
    #driver.execute_script(f"arguments[0].innerText = {ra_inp[0]}", ra)
    
    
    dec = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[4]/input[2]")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(dec)
    for i in range(3):
        action.move_to_element(dec).click()
    action.perform()
    dec.send_keys(dec_input)
    #driver.execute_script(f"arguments[0].innerText = {de_inp[0]}", dec)
    
    
    rms = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[15]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(rms)
    for i in range(3):
        action.move_to_element(rms).click()
    action.perform()
    rms.send_keys(20)
    
    fudge = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[19]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(fudge)
    for i in range(3):
        action.move_to_element(fudge).click()
    action.perform()
    fudge.send_keys(4)
    
    polarization = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[22]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(polarization)
    for i in range(3):
        action.move_to_element(polarization).click()
    action.perform()
    polarization.send_keys("01h 00m 00s")
    
    calculate = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[26]/td/input[1]")
    calculate.click()
    
    time.sleep(3)
    
    
    download_pdf = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[26]/td/input[3]")
    download_pdf.click()
    
def band3(ra_input, dec_input):

    search_source = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[4]/select")
    
    select = Select(driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[4]/select'))
    
    # select by visible text
    select.select_by_visible_text("Band-3 (260-500 MHz)")
    
    
    ra = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[4]/input[1]")
     
    # Sending input text to search field
    action = ActionChains(driver)
        
    action.double_click(ra)
    for i in range(3):
        action.move_to_element(ra).click()
    action.perform()
    
    ra.send_keys(ra_input)
    #driver.execute_script(f"arguments[0].innerText = {ra_inp[0]}", ra)
    
    
    dec = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[10]/td[4]/input[2]")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(dec)
    for i in range(3):
        action.move_to_element(dec).click()
    action.perform()
    dec.send_keys(dec_input)
    #driver.execute_script(f"arguments[0].innerText = {de_inp[0]}", dec)
    
    
    rms = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[15]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(rms)
    for i in range(3):
        action.move_to_element(rms).click()
    action.perform()
    rms.send_keys(30)
    
    fudge = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[19]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
    
    polarization = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[22]/td[4]/input")
    #action chain object
    action = ActionChains(driver)
        
    action.double_click(polarization)
    for i in range(3):
        action.move_to_element(polarization).click()
    action.perform()
    polarization.send_keys("00h 00m 00s")
        
    action.double_click(fudge)
    for i in range(3):
        action.move_to_element(fudge).click()
    action.perform()
    fudge.send_keys(5)
    
    calculate = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[26]/td/input[1]")
    calculate.click()
    
    time.sleep(3)
    
    
    download_pdf = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[26]/td/input[3]")
    download_pdf.click()
#%%
band5(ra_inp[0], de_inp[0])
band4(ra_inp[0], de_inp[0])
band3(ra_inp[0], de_inp[0])

#%%
