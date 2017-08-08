class Point:

    def __init__(self,x,y):
        self.x = x;
        self.y = y;

    def swap(self):
        temp = self.x;
        self.x = self.y;
        self.y = temp;
        print "After Swapping : ";
        print "\nValue of X: ",self.x,"\nValue of y:",self.y;

x = input("Enter Value for X: ");
y = input("Enter Value for Y:");

print "\nBefore Swapping: ";
print "\nValue of X: ",x,"\nValue of Y: ",y;

pt = Point(x,y);
pt.swap()