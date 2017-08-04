def gcd(a,b):
    rem = a%b;
    if(rem==0):
        return b;
    else:
        return(gcd(b,rem));
a = int(raw_input("\nEnter num1:"));
b = int(raw_input("\nEnter num2:"));

result = gcd(a,b);

print"\nGCD of",a,"and",b,":",result;