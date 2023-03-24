from selenium import webdriver
import time
import pandas as pd
import os

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url1='https://www.linkedin.com/jobs/search?keywords=Marketing%20Data%20Analyst&location=Berlin%2C%20Berlin%2C%20Germany&geoId=106967730&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'


driver = webdriver.Chrome(executable_path=r'C:\\Users\\Default\\Desktop\\chromedriver.exe')
driver.implicitly_wait(10)
driver.get(url1)
y=driver.find_elements_by_class_name('results-context-header__job-count')[0].text
type(y)
n=pd.to_numeric(y)
n

#Loop to scroll through all jobs and click on see more jobs button for infinite scrolling

i = 2
while i <= int((n+200)/25)+1: 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    
    try:
        send=driver.find_element_by_xpath("//button[@aria-label='Load more results']")
        driver.execute_script("arguments[0].click();", send)   
        time.sleep(3)
    
        
         #buu=driver.find_elements_by_tag_name("button")
         #x=[btn for btn in buu if btn.text=="See more jobs"]
         #for btn in x:
                #driver.execute_script("arguments[0].click();", btn)
                #time.sleep(3)
        
                                                 


            
    except:
        pass
        time.sleep(5)


#Create empty lists for company name and job title

companyname= []
titlename= []


#Find company name and append it to the blank list

try:
    for i in range(n):
        company=driver.find_elements_by_class_name('base-search-card__subtitle')[i].text
        companyname.append(company)
except IndexError:
    print("no")

len(companyname)


#Find title name and append it to the blank list
try:
    for i in range(n):
        title=driver.find_elements_by_class_name('base-search-card__title')[i].text
        titlename.append(title)
except IndexError:
    print("no")

len(titlename)
#Create dataframe for company name and title

companyfinal=pd.DataFrame(companyname,columns=["company"])
titlefinal=pd.DataFrame(titlename,columns=["title"])

x=companyfinal.join(titlefinal)

x

#Save file in your directory

x.to_csv('linkedin.csv')

#Find job links and append it to a list

jobList = driver.find_elements_by_class_name('base-card__full-link')
hrefList = []
for e in jobList:
    hrefList.append(e.get_attribute('href'))

#for href in hrefList:
    #link.append(href)
    
hrefList

linklist=pd.DataFrame(hrefList,columns=["joblinks"])
linklist.to_csv('linkedinlinks.csv')
#Close the driver

driver.close()