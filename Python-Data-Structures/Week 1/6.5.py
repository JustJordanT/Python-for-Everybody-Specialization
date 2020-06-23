#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

thing0 = text.find('    ')
thing1 = text.find('0',thing0)
thing3 =text[23:thing1+6]
thing4 = float(thing3)
print(thing4)