class Area:
    def __init__(self,radius):
        self.radius = radius ;
    def area(self):
        a = 3.14 * radius * radius ;
        print "\nArea of Circle:",a;
radius = input("\nEnter Radius: ");
a1 = Area(radius);
a1.area();

