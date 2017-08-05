def happy(n):
    past = set()
    while n!=1:
        n = sum(int(i)**2 for i in str(n))
        #print(n)#uncomment the code to see the iterated no.
        if n in past:
            return False
        past.add(n)
    return True
number = int(raw_input("Enter a Number : "))

if happy(number):
    print(str(number) + " is a Happy Number ")
else:
    print(str(number) + "is not a Happy Number")