string = raw_input("Enter a string to reverse :")
#using Generator Expression
print" ".join(string[c] for c in xrange(len(string) - 1, -1,-1))