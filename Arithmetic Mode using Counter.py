from collections import Counter
def modes(Values):
    count = Counter(Values)
    best = max(count.values())
    return[k for k,v in count.items()if v == best]
num_array = list()

num = raw_input("Enter how many elements you want : ")

print 'Enter numbers : '
for i in range(int(num)):
        n = raw_input("num"+str(i+1)+":")
        num_array.append(int(n))
print "Arithmentic Mode : " + str(modes(num_array))