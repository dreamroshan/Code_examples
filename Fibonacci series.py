def fibonacci(n):
    a = 0
    b = 1
    for i in range(0,n):
        temp = a
        a = b
        b = temp + b
    return a
# take input from the user
nterms = int(input("How many terms?"))

#Display the first 15 Fibonacci numbers.
for c in range(0,nterms):
    print(fibonacci(c));