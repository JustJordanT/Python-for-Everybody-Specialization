
"""7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name."""
#Count the lines, looking at only the floating points compute the avarage of those lines.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
#Counter for the line counter. starts at `None` then for ever loop that passes if the line contains the `X-DSPAM` program will add + 1 to the counter.
count = 0
#For loop for counting the number of lines and computing the avg.
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print(line)
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
print(line)
print('Done:' , count)