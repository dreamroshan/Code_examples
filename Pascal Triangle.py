import math;

def combination(n, r):
    return int((math.factorial(n))/((math.factorial(r))* math.factorial(n - r)));

def for_test(x,y):
    for y in range(x):
        return combination(x,y);

def pascals_triangle(rows):
    result = [];
    for count in range(rows):
        row = [];
        for element in range(count + 1):
            row.append(combination(count,element));
        result.append(row);
    return result;
num =int(raw_input("\nEnter number of rows till u want Pascal Triangle: "));
for row in pascals_triangle(num):
    print(row);

