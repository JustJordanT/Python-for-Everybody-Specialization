import xml.etree.ElementTree as ET


url = input("Enter url: ")
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
# x = tree.findall('.//count')

stuff = ET.fromstring(data)
counts = tree.findall('comments/comment/count')

total = 0
for count in counts:
    total += int(count.text)

print('total: ',total)
# for n in lst:
#     number = int(n)
#     count = count + number
# print('Sum: ',count)