# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = ('http://py4e-data.dr-chuck.net/known_by_Lili.html')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')



# # Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(len(tag.get('href', None)) , (tag.get('href', None)))

link = input('Enter URL: ')
count=int(input('Enter counts: '))
pos=int(input('Enter line: '))

print('Retriving: ',link)
for i in range(0,count):
    html=urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags=soup('a')

    link=tags[pos-1].get('href')

result=tags[pos-1].contents[0]
print(result)