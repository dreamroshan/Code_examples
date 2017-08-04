num = int(raw_input("\nEnter num: "));

print "\nPrime number : " ;
for i in range(1,(num+1)):
    flag=0;
    for j in range(2,i):
        if(i%j == 0):
            flag=1;
            break;
    if(flag==0):
        print"\n",i;