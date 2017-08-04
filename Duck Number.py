number = str(raw_input("Enter a number to check whether its a Duck number or not : "))

c = 0

#to check whether number contains zero or not
for i in range(1,len(number)):
    ch = number
    if ch == '0':
        c+=1

f = number[0]

print
if c > 0 and f!= '0':
    print number,"is a Duck number"
else:
    print number,"is not a Duck number"