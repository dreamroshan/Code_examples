def Palindrome_Number(n):

    m=n
    a = 0
    while(m!=0):
        a = m % 10 + a* 10
        m = m / 10

    if(n == a):
        print('%d is a palindrome number'%n)
    else:
        print('%d is not a palindrome number'%n)

n = input('Enter Number to check for palindromee ')
Palindrome_Number(n)