import urllib.request, urllib.parse, urllib.error,re
from bs4 import BeautifulSoup

url= input("Enter the Url: ")
count = int(input("Enter Count: "))
position = int(input("Enter Position: "))
i = 0


while (i < count):
    #this will open the url and collect the data in fhand
    fhand = urllib.request.urlopen(url)
#this is gonna remove the extratags and beautify it in simple tags
    soup = BeautifulSoup(fhand, "html.parser")
    tags = soup('a') #extract all the a tags from the data & returns an array

    url = tags[position-1].get("href", None) #extracting href tags from the tags array at a given position
    print(tags[position-1].get("href", None))
    i= i + 1
print(tags[position-1].contents[0])
