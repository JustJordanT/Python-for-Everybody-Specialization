# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fr = fh.read()
sr =fr.rstrip()
print(fr.upper())