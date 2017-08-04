number = int(raw_input("Enter a number to check whether its Disarium number or not : "))

c = 1
x = number
sum = 0
rev = 0

while number > 0:
    rev = rev * 10 + number % 10
    number = number / 10
while rev > 0:
    sum = sum + pow(rev % 10 , c)
    c +=1
    rev = rev / 10
print
if(sum == x):
    print x,"is Disarium Number"
else:
    print x,"is not Disarium Number"
