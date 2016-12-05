# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Nur', cell_overwrite_ok = True)

chrome_path=r"C:\Users\yera\Desktop\\WinPython-64bit-3.4.3.7\python-3.4.3.amd64\Scripts\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("https://nur.kz")

"""
news = [i.text for i in driver.find_elements_by_xpath('//div[@class="news clearAfter pl mb"]//span[@class="sc-icon"]')] #[3, 4, 0] #comments
news_link = [j.get_attribute("href") for j in driver.find_elements_by_xpath('//div[@class="news clearAfter pl mb"]/a')] #[https://tengrinews.kz, https://tengrinews.kz]
"""
cnt_coms = [cnt.text for cnt in driver.find_elements_by_xpath('//div[@class="news news-list__item"]/p[@class="news-list__comments"]')]
links = [a.get_attribute('href') for a in driver.find_elements_by_xpath('//div[@class="news news-list__item"]/a')]

for j in range(0, 4):
    if j==0:
        worksheet.write(0, j, "title")
    elif j==1:
        worksheet.write(0, j, "comments")
    elif j==2:
        worksheet.write(0, j, "authors")
    elif j==3:
        worksheet.write(0, j, "likes")



cnt=1	

for i in range(len(cnt_coms)):
    if cnt_coms[i] != '0':                                                                                                         
        driver.get(links[i])  
        comms  = driver.find_elements_by_xpath('//li[@class="answer__item"]')
        
        titles = driver.find_element_by_xpath('//div[@class="r"]//h1').text
        worksheet.write(i + len(comms) + 1, 0, titles)
        for comm in comms:     
            for k in range(1, 7):
                if k==1:
                     texts = comm.find_element_by_xpath('.//div[@class="answer__body"]/div[@class="answer__text"]').text
                     worksheet.write(cnt, k, texts)   
                elif k==2:
                    auth  = comm.find_element_by_xpath('.//div[@class="answer__caption cf"]/span[@class="answer__name"]').text
                    worksheet.write(cnt, k, auth)
                elif k==3:	
                    likes = comm.find_element_by_xpath('.//div[@class="answer__caption cf"]/span[@class="answer__vote"]/div[@class="answer__up"]/span[@class="answer__value"]').text
                    worksheet.write(cnt, k, likes)       
                elif k==4:
                    worksheet.write(cnt, cnt)		
            cnt=cnt+1	
            
         	
workbook.save('era.xls')
