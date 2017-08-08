alist = list(map(int,raw_input("Enter numbers: ").split()))

smallest=alist[0]

for small in alist:
    if small < smallest:
        smallest=small

print
print "Smallest number is : ",smallest