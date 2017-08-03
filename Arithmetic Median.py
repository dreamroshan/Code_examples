def median(array):
    srtd = sorted(array)
    print "Elements in sorted order: "+str(srtd)
    alen = len(srtd)
    return 0.5*(srtd[(alen-1)//2] + srtd[alen//2])
num_array = list()
num =raw_input("Enter how many elements you want: ")
print 'Enter numbers : '
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+":")
    num_array.append(float(n))
print "Arithmetic Median : " +str(median(num_array))