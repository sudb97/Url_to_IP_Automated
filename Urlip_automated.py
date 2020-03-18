#importing packages
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common import keys 
from selenium.webdriver.common.keys import Keys
import time
import re
import xlwt
from xlwt import Workbook

""" converting the text file data to a list for easy access"""
print(r"Enter the path of the text file which contains the list of URLs (Ex:D:\Python Projects\ULR to IP automated\URL.txt)")
url_path=input()
df = pd.read_csv(url_path)
links = list(df["links"])
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'URLs')
sheet1.write(0,1,'IPs')

# to open the browser and redirect to the website url 
print(r"Provide the path of the geckodriver.exe in the system (Ex: C:\Users\..\..\geckodriver.exe)")
path=input()
leap=0
for i in range(0,len(links)):
    driver = webdriver.Firefox(executable_path=path) #path of the gecodriver.exe installed in the system
    driver.get('https://www.ipvoid.com/find-website-ip/')
    time.sleep(5)
    box =driver.find_element_by_id('websiteAddr')
    box.send_keys(links[i])
    box.send_keys(Keys.RETURN)
    time.sleep(7)
    #ips = driver.find_element_by_xpath("/html/body/section[2]/div/div/div/div[1]/div/textarea").text #by class_name not used
    ips = driver.find_element_by_css_selector('textarea.form-control').text
    ip1= ips.splitlines()
    l=len(ip1)
    driver.close()
    for j in range(0,l):
        ip =re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip1[j] )
        sheet1.write(leap+j+1, 0, links[i])
        sheet1.write(leap+j+1, 1, ip[0])
    leap=leap+l
print(r"Enter the destination path of the file to be saved (Ex: D:\\Python Projects\\ULR to IP automated\\):")
path_wb1=input()
path_wb2=path_wb1+'\\url_ip.xls'
wb.save(path_wb2)
print(r"Successfully completed!!! The xls file is saved in:"+path_wb2)
