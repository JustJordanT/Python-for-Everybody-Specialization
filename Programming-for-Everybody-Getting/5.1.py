num = 0
tot = 0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try:
       fval = int(sval)
    except:
        print('Invaled Input')
        continue

    num = num + 1
    tot = tot + fval
print(tot,num)