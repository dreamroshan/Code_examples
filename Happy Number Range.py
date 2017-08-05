def happy(n):
    past = set()
    while n!=1:
        n = sum(int(i)**2 for i in str(n))
        #print(n)#uncomment the code to see the iterated no.
        if n in past:
            return False
        past.add(n)
    return True
number = int(raw_input("Enter the upper limit for happy numbers : "))

print("Happy Numbers between the range 1 -" +str(number)+":")
happyn = []
for x in range(1,number):
    if(happy(x)):
        happyn.append(x)
print(happyn)