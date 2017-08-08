'''
@author : CreativeCub
'''

var1 = "this is python programming"
var2 = "this is is python"

#Title - All words begin with uppercase and the rest are lowercase
print "Title:",var1.title()

#Counts how many times str occurs in string or in a substring
#of string if starting index beg and ending index end are given
print "Count of 'is : ",var2.count('is')

#Count 'is' between 0 to 5 range
print "Count of 'is' with range: : ",var2.count('is',0,5)

#Determines if string or a substring of string (if starting
#index beg and ending index end are given)ends with suffix;
#returns true if so and false otherwise
print "String ends with 'python' : ",var2.endswith('python')

#Determines if string or a substring of string (if starting
#index beg and ending index end are given) starts with substring
#str; returns true if so and false otherwise
print "String starts with 'this': ",var2.startswith('this')

#Determine if str occurs in string or in a substring of string
#if starting index beg and ending index end are given returns
#index if found and -1 otherwise
print "Is 'python' there is var1: ",var1.find('programming')
print "Is 'python' there is var2: ",var2.find('programming')



