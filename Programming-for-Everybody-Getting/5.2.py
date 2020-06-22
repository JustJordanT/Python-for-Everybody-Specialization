min = None
max = None
while True:
    num = input("Enter a number: ")

    #input
    if num == "done" : break
    if len(num) == 0 : continue

    try:
    	num = int(num)
    	if min is None or min > num :
    		min = num;
    	if max is None or max < num :
    		max = num;

    except:
    	print ("Invalid input")

print ("Maximum is", max)
print ("Minimum is", min)
