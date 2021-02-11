import urllib.parse, urllib.request,urllib.error,json
import ssl

url= input( "Enter the Url: ")
print("Retrieving ",url)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen(url,context = ctx)

data = fhand.read().decode()
print("Retrieved ",len(data)," characters")
while True:

    if len(data) < 1:
        print("====File doesn't have any Data====")
        break

#This will create a dictionary with two elements comment and note
    info = json.loads(data)
    sum = 0
#This will print the elements in dictionary comments : that's again a list of dictionaries with Name and count
#print(info['comments'])
    for item in info['comments']:
        sum = sum + int(item['count'])
#printing the final count and beaking the loop
    print(sum)
    break
