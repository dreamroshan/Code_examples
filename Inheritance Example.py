class Parent(object):
    def __init__(self):
        print "\nParent class constructor...";
    def display(self):
        print "\nParent class method...";
class Child(Parent):
    def __init__(self):
        print "\nChild class constructor...";

    def display(self):
        super(Child,self).display()
        print "\nChild class method...";

p = Parent();
c = Child();
c.display();
