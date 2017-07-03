#Find running movie on imdb and their collections 
#Using BeautifulSoup,requests,and lxml parser
import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.imdb.com/")
c=r.content
soup=BeautifulSoup(c,"lxml")

movie=soup.find_all("div",{"class":"title"})
details=[]
for a in movie:
    for d in a:
        details.append(d.string)
#for i in range(len(details)):
 #   print(details[i])
contents=[]
for i in range(len(details)):
    if details[i]!=' ':
       contents.append(details[i])
        #print(i,"-->",details[i])
print("Movie Name","-->","Collections")
for i in range(0,len(contents)-1,2):
    print(contents[i],"-->",contents[i+1])
