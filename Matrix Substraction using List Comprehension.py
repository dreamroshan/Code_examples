print("Enter the value of row : ")
x=int(raw_input())

print("Enter the value of column : ")
y=int(raw_input())

a=[[0 for row in range(0,x)]for col in range(0,y)]
b=[[0 for row in range(0,x)]for col in range(0,y)]
result = [[0 for row in range(0,x)]for col in range(0,y)]

print
print "Enter elements of first matrix : "
for i in range(x):
        for j in range(y):
            a[i][j] = int(raw_input())
print
print "Enter the elements of second matrix : "
for i in range(x):
    for j in range(y):
        b[i][j]=int(raw_input())

print
print"Elements of First matrix is : "
for row in a:
    print(row)

print
print"Elements of Second matrix is : "
for row in b:
    print(row)

#Using list comprehension
result = [[a[i][j]-b[i][j] for j in range(len(a[0]))]for i in range(len(a))]

print
#print the Substraction of 2 matrix
print "Substraction is :"
for r in result:
    print(r)