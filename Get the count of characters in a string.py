para = "Hi welcome to python dictionary example"

#Initialising dictionary
chrCount = {}

#getting each character from the variable para
for i in para:
    #strip function will remove the pre and post spaces from a string variable
    if i.strip() == " ":
        continue
    #if key already exist in dictionary chrCount. add 1 to the value of the element
        if(i in chrCount):
            chrCount[i]=chrCount[i]+1
    #newly adding an key with value as 1 into the dictionary chrCount
    else:
        chrCount[i] =1
print chrCount