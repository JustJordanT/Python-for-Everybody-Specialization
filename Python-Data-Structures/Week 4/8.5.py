
"""8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt"""


"""fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fname:
    line = line.split()
    for emails in line:
        if not line.startswith('FROM'): continue
        if line.startswith('FROM'):
            count = count + 1
print(line)
print("There were", count, "lines in the file with From as")"""


file = open('mbox-short.txt')
fh = file
count = 0
for line in file:
    line = line.rstrip()
    if not line.startswith('From '): continue
    if line.startswith('From '):
        count = count + 1
    emails = line.split()
    print(emails[1])
print('There were', count, 'lines in the file with From as the first word')