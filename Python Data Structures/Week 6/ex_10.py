fname = input('Enter File Name: ' )
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #idiom: retrive/create/update counter
        di[w] = di.get(w,0) + 1

#PRINTS THE WHOLE DICT
# print(di)

# x = sorted(di.items())
# print(x[:6]
tmp = list()
for k,v in di.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)
# print('Filpped:' , tmp)
tmp = sorted(tmp, reverse=True)
# print('Sorted: ', tmp[:5])

for v,k in tmp[:5] :
    print(k,v)