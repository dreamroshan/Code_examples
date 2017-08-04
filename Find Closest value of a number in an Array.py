closest = 0

array = list()
num = raw_input("Enter number of elements : ")

print
print 'Enter'+str(num)+ 'numbers in array : '
for i in range(int(num)):
    n = raw_input("num" +str(i + 1)+":")
    array.append(int(n))

print
print "Numbers are : "
print array

print
find = int(raw_input("Enter Number to find closest value : "))

distance = abs(closest - find)

for i in range(1,len(array)):
    distanceI = abs(array[i]-find)
    if distance > distanceI:
        closest = array[i]
        distance = distanceI
print
print "Closest Value is : ",closest
