print("Enter the value of row and column of first matrix : ")
x=int(raw_input())
y=int(raw_input())
a,b = x,y

X =[x[:] for x in [[0]*y]*x]

print "Enter elements of first matrix : "
for i in range(a):
    for j in range(b):
        X[i][j]=int(raw_input())
print
print"Enter the value of row and column of second matrix :"
c=int(raw_input())
d=int(raw_input())
m,n = c,d

Y = [c[:] for c in [[0]*d]*c]

print "Enter elements of second matrix : "
for i in range(m):
    for j in range(n):
        Y[i][j]=int(raw_input())
print
print "Elements of First matrix is : "
for row in X:
    print row

print
print "Elements of Second matrix is : "
for row in Y:
    print row

#using list comprehension
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X ]

print
print "Matrix Multiplication : "
for r in result:
    print(r)
