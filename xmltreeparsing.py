import urllib.request, urllib.parse, urllib.error, xml.etree.ElementTree as ET
import ssl

url = input("Enter Location: ")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen(url, context=ctx)
data = fhand.read()

tree = ET.fromstring(data)

counts= tree.findall('.//count')


print ("Total Counts: ",len(counts))
#i = 0
sum = 0
for count in counts:
    sum = sum + int(count.text)

print ( "Sum: ", sum)
