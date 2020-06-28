import re


fname = input('Enter File Name: ' )
if len(fname) < 1 : fname = '42.txt'
hand = open(fname)

y = re.findall('[0-9]+', hand)
print(sum(y))