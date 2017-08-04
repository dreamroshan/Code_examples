side = int(input("Enter the length of the diamond pattern : "))

print

for x in list(range(side)) + list(reversed(range(side-1))):
    print('{: <{w1}}{:*<{w2}}'.format('','',w1 = side-x-1,w2 = x*2+1))