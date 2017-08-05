def k(n):
    n2 = str(n**2)
    for i in range(len(n2)):
        a,b = int(n2[:i] or 0), int(n2[i:])
        if b and a + b == n:
            return n
number = int(raw_input("Enter a upper limit for Kaprekar Numbers:"))
print("Kaprekar Number between the range 1 -"+str(number)+":")

print([x for x in range(1,number)if k(x)])
