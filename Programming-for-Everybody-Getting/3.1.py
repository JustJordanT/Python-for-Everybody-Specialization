hrs = input("Enter Hours:")
rt = input("Enter Rate:")
try:
    fh = float(hrs)
    fr = float(rt)
except:
    print("Please enter a numerical input!")
if fh > 40 :
    reg = fh * fr
    otp = (fr * 2.5)
    xp = reg + otp
else :
    xp = fh * fr
print("Pay: ",xp)