def perfectsquare(x):
    ans = 0
    if x >= 0 :
        while ans*ans < x :
            ans = ans + 1

        if ans*ans != x:
            print x,'is not a perfect square.'
        else:
            print x, 'is a perfect square.'
    else:
        print x,'is not a positive number.'
number = int(raw_input("Enter a number : "))

print

perfectsquare(number)