# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#Needed Output.
"""
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""





# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

# di = dict()
# for line in handle:
#     if line.startswith('From' ):
#         line = line.rstrip()
#         wds = line.split()
#         print(wds[6:6])
#         time = wds[0]
#         for time in wds:
#             di[time] = di.get(time,0) + 1
# print(time)
# # print(line

# fname = input('Enter File Name: ' )
# if len(fname) < 1 : fname = 'mbox-short.txt'
# hand = open(fname)

# di = dict()
# for lin in hand:
#     if lin.startswith('From '):
#         lin = lin.rstrip()
#         wds = lin.split()
#         time = wds[5]
#         hour = time[0:2]
#         print(hour)
#         for hour in time:
#             di[hour] = di.get(hour,0) +1

#PRINTS THE WHOLE DIC
# print(di)

# x = sorted(di.items())
# print(x[:6]
# tmp = list()
# for k,v in di.items():
#     print(k,v)
#     newt = (v,k)
#     tmp.append(newt)
# print('Filpped:' , tmp)
# tmp = sorted(tmp, reverse=False)
# print('Sorted: ', tmp)
# for v,k in tmp:
#     print(k,v)




name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

tt = list()
dd = dict()
for line in handle:
    if line.startswith("From "):
	    line = line.rstrip()
	    words = line.split()
	    time = words[5]
	    hour = time[0:2]
	    dd[hour] = dd.get(hour,0) +1
#for key, val in d.items():
tt = dd.items()
tt = sorted(tt)
for k,v in tt:
    print (k,v)