name = input("Enter file:")
dict = {}
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if line.startswith("From "):
	    line = line.rstrip()
	    words = line.split()
	    email = words[1]
	    if email not in dict:
		    dict[email] = 1
	    else:
	        dict[email] += 1
print(email)

bigname = None
bigcount = None
for mail in dict:
   if bigcount == None or bigcount < dict[email]:
      bigname = email
      bigcount = dict[email]
print ('%s %d' % (bigname, bigcount))