#To know latest News from AKTU website
# Python Script using BeautifulSoup, requests and lxml parser
#Latest Aktu News Portal
#Ashutosh Pandey

import bs4 as bs
import urllib.request
import lxml
my_url="https://erp.aktu.ac.in/Webpages/Public/Circular/CircularForWebsite.aspx"
page=urllib.request.urlopen(my_url).read()
soup=bs.BeautifulSoup(page,"lxml")
detail=soup.table
data=detail.find_all("a")
for a in data:
    print(a.text)

         
