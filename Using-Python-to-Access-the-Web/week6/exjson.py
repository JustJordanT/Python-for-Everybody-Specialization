import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url: ")
data = urllib.request.urlopen(url).read()

counts = json.loads(data)

count = 0
for n in counts['comments']:
    number = int(n['count'])
    count = count + number
print('Sum: ',count)




