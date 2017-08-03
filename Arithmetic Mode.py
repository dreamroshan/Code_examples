from collections import defaultdict
def modes(values):
    count = defaultdict(int)
    for v in values:
        count[v]+=1
    best = max(count.values())
    return ([k for k,v in count.items()if v == best])
num_array = list()

num = raw_input("Enter how many elements you want: ")

print 'Enter numbers :'
for i in range(int(num)):
    n = raw_input("num"+str(i+1)+":")
    num_array.append(int(n))
print "Arithmetic Mode:" +str(modes(num_array))