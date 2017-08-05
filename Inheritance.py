class Parent():
    def __init__(self,last_name,eye_color):
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print(self.last_name + " eye color is " + self.eye_color)

class Child(Parent):
    def __init__(self,last_name,eye_color,number_of_toys):
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        print(self.last_name + " eye color is " + self.eye_color +" and no of toys are " + str(self.number_of_toys) )

avinash = Parent("Shetty","Brown")

rahul = Child("Shetty","Black",5)
avinash.show_info();
rahul.show_info()
print(avinash.eye_color)
print(rahul.eye_color)