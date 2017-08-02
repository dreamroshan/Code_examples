# Definintion of the function

def amicable_numbers(x,y):
    sum_x=0
    sum_y=0
    for i in range(1,x):
        if x%i==0:
            sum_x+=i
    for k in range(1,y):
        if y%k==0:
            sum_y+=k

    return sum_x==y and sum_y==x

#Program body

n_1=int(raw_input('Enter number 1: '))
n_2=int(raw_input('Enter number2: '))

print
if amicable_numbers(n_1,n_2):
    print 'The numbers are Amicable! : )'
else:
    print 'The numbers are Not Amicable :('