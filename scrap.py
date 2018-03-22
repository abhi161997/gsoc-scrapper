##import requests
##import scrapy
from bs4 import BeautifulSoup
link = "https://summerofcode.withgoogle.com/organizations/"

#r = requests.get(link)
#soup = BeautifulSoup(r.content,"lxml")



## real code starts here

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r'D:\\python-driver\\geckodriver-v0.20.0-win64\\geckodriver.exe')
#driver.get('https://www.youtube.com')
driver.get(link)
html = driver.execute_script("return document.documentElement.outerHTML")
html_source = html.page_source
print(html_source)
#driver.quit()
#soup = BeautifulSoup(html_source,'html.parser')



#print(soup)

#orgs = soup.findAll('div',{'class':'organization-card__container flex-xs-100 flex-sm-50 flex-33'})
#tech = soup.findAll('h3',{'class':'organization-card__tag-title md-body-1'})
#print(tech)
#tech_value = soup.findAll('li',{'class':'organization__tag organization__tag--technology'})
#print(tech_value)