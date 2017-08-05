def k(n):
    n2 = str(n**2)
    for i in range(len(n2)):
        a,b = int(n2[:i] or 0), int(n2[i:])
        if b and a + b == n:
            return n

number = int(raw_input("Enter number:"))
if k(number):
    print(str(number)+" is Kaprekar Number ")
else:
    print(str(number)+ " is not a Kaprekar Number ")

