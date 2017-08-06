def lucas(n):
    a = 2
    b = 1
    for i in range(0,n):
        temp = a
        a = b
        b = temp + b
    return a

#take input from the user
nterms = int(input("How many terms?"))

print
#Display the first n lucas numbers.
print "Lucas Series : "
for c in range(0,nterms):
     print(lucas(c))