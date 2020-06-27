fname = input('Enter File Name: ' )
if len(fname) < 1 : fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
        #if the key is not there the is zero.
        # oldcount =di.get(w,0)
        # print(w,'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
            #idiom: retrive/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w, 'new' , di[w])
# print(di)

#now  to find the most common code.
largeest = -1
theword = None
for k,v in di.items() :
    # print(k,v)
    if v > largeest:
        largeest = v
        theword = k
print('Done', theword, largeest)
