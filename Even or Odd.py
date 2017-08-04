i = int(raw_input("Enter a Number"))

def is_even(i):
    return (i%2)== 0
if is_even(i):
    print(str(i)+"is an Even Number")
else:
    print(str(i)+"is an Odd Number")