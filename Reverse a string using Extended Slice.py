string = raw_input("Enter a string to reverse : ")

#Using Extended Slice Syntax
""" If start is omitted it defaults to 0 and if stop is omitted it defaults to the length of the string.
A step of -1 tells Python to start counting by 1 from the stop until it reaches the start."""

print string[::-1]