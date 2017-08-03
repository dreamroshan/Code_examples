input = int(raw_input("Enter a number : "))

square = input * input

v = pow(10,len(str(input)))

print
if(square%v)==input:
    print input,"is an Automorphic Number "
else:
    print input,"is not an Automorphic Number"