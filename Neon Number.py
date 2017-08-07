number = int(raw_input("Enter a number: "))


s = 0
square = str(number * number)

for i in range(0,len(square)):
    s += int(square[i:i+1])

print
if(s == number):
    print number,"is a Neon Number"
else:
    print number,"is not a Neon Number"
