class A(object):
    def __init__(self,a):
        self.a = a;

    def display(self):
        print "\nValue of A: ",a;

class B(A):
    def __init__(self,a,b):
        super(B,self).__init__(a);
        self.b = b;

    def display(self):
        super(B,self).display();
        print "\nValue of B: ",b;

a=100;
b=200;
b1 = B(a,b);
b1.display();

