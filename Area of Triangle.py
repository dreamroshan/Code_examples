# Area of Triangle (1/2 * base * height)

def areaoftriangle(base,height):
    area = 0.5 * base * height
    return area

base = float(raw_input("Enter base of the triangle : "))
height = float(raw_input("Enter height of the triangle : "))

print 'The area of the triangle is %0.2f' %areaoftriangle(base,height)