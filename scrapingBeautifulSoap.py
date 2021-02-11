import urllib.request, urllib.parse, urllib.error,re
from bs4 import BeautifulSoup

url= input("Enter Url:")

fhand = urllib.request.urlopen(url)
sum = 0
count = 0
soup = BeautifulSoup(fhand, "html.parser")
tags = soup('span')

print("Here we print Tags       : ")
print(tags)
print(soup)

for tag in tags:
    sum= sum + int(tag.contents[0])
    count= count + 1
print("Count ",count)
print("Sum ",sum)
