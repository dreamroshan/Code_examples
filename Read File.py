from os.path import exists

print "Type the filename : "
file = raw_input(" > ")
if exists(file):
    txt_again = open(file,'r')
    print txt_agian.read()
else:
    print "no such file"