import http.client,json

conn = http.client.HTTPSConnection("dm-us.informaticacloud.com")
payload = "{\n\"username\":\"vc@gmail.com\",\n\"password\":\"Fastrack@234\"\n}"
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/saas/public/core/v3/login", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

info= json.loads(data.decode("utf-8"))

#print("Info type is: ", type(info['userInfo']))

item = info["userInfo"]
print(info["userInfo"]["sessionId"])
    #sessionId = item["sessionId"]
    #print("The session Id is: ", sessionId)
