import urllib.request,urllib.parse,urllib.error, ssl, json

api_key= False


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

param = dict()

while True:
    address = input("Enter Address:")
    #print ("You are looking geocode for address-->", address)

    param['key']= api_key
    param['address']= address
    url = serviceurl + urllib.parse.urlencode(param)

    print("Retrieving : ",url)

    fhand = urllib.request.urlopen(url, context=ctx)

    data = fhand.read().decode()
    print("Retrieved ",len(data)," characters")
    #print(data)

    try:
        info = json.loads(data)
    except:
        info = None
        #print(json.dumps(info, indent=4))
    if not info or 'status' not in info or info['status'] != 'OK':
        print("+++Wrong Data+++")
        print(info)
        continue

    print ("Place Id",info['results'][0]['place_id'])
    break
