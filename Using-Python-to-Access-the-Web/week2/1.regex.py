import re


# fname = input('Enter File Name: ' )
# if len(fname) < 1 : fname = '42.txt'
# hand = open(fname)

count = 0
hand = open('41.txt')
line = hand.read()
x = re.findall('[0-9]+', line)
for n in x:
    number = int(n)
    count = count + number
print(count)
    # if len(x) > 0:
    #     type(x) 
    #     for y in range(len(x)):
    #         z = x[y]
    #         print("".join(z))
        #
# y = re.findall('[0-9]+', hand)
# print(sum(y))