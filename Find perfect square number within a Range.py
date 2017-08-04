import math

def perfectsquare(start,end):
    sum1 = 0
    for i in range(start,end):
        s = float(math.sqrt(i))
        n = int(math.floor(s))
        if(s ==n):
            print i;
            sum1 += i
    print
    print "Sum of the perfect square numbers between the range",start,"to",end,"are : ",sum1
start = int(raw_input("Enter starting value of the range : "))
end = int(raw_input("Enter ending value of the range : "))

print
print "The Perfect Square present between the range",start,"to",end,"are :"
perfectsquare(start,end)