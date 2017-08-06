a=int(raw_input("Enter a number: "))

n=map(int,'a')

while a>n[0]:n=n[1:]+[sum(n)]

print
if(a==n[0])and(a>9):
    print a,"is a Keith Number"
else:
    print a,"is not a Keith Number"