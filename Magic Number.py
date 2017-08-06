def isMagic(n):
    s = 0
    d = 0
    number = n
    flag = 0
    while flag == 0:
        while n%10 == 0:
            n /= 10

        while n% 10 != 0 or n > 0:
            s += (n % 10)
            n /= 10

        if s >= 10:
            n = s
            s = 0
        else:
            flag = 1
    if s == 1:
        print number,"is a Magic Number"
    else:
        print number,"is not a Magic Number"

number = int(raw_input("Enter a number :"))

print isMagic(number)