# Take decimal number from user

dec = int(input("Enter a number :"))

#convert decimal to binary
bin(dec)

#convert decimal to octal
oct(dec)

#convert decimal to hexadecimal
hex(dec)

print
print "The decimal value", dec,":"
print "In binary is :",format(dec,'b')
print "In octal is: ",format(dec, 'o')
print "In hexadecimal is :",format(dec, 'x')