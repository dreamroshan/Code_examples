# copy content from one file to other.

import shutil

shutil.copyfile("abc.txt","xyz.txt")

#If no mode is specified,
# 'r' ead mode is assumed by default

f = open('xyz.txt')

print "The contents of another file:"
print

while True:
    line = f.readline()
    #Zero length indicates EOF
    if len(line) == 0 :
        break
    print line,
# close the file
f.close()