class AgeNegative(Exception):
    def display(self):
        print "\nAge is negative...";

age = int(raw_input("\nEnter your age: "));
try:
    if(age<0):
        raise AgeNegative();
    else:
        print"\nNo Exception Raised...";
except AgeNegative,e:
    e.display();