array = list()
num = raw_input("Enter number of elements : ")

print
print 'Enter'+str(num)+'numbers in array :'
for i in range(int(num)):
    n = raw_input("num" + str(i + 1)+ ":")
    array.append(int(n))

print
print "Numbers are : "
print array

print
find = int(raw_input("Enter Number to find closest value : "))

print

#using lambda function
takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))

print "Closest Value is : ",takeClosest(find,array)
