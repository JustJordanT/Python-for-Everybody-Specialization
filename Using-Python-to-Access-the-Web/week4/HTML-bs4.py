# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0
url = ('http://py4e-data.dr-chuck.net/comments_695397.html')
html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
x = re.findall(b'>([0-9]+)', html)
# print(x)
# Retrieve all of the anchor tags
for n in x:
    number = int(n)
    count = count + number
print('Sum: ',count)