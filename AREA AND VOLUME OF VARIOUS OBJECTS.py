import math

#Rectangle area
def rectangle_area(length,width):
    
    if length<=0 or width <=0:
        print("Error! Enter positive integers.")
    else:
        return length*width    
l=int(input("Enter the length: "))
w=int(input("Enter the width: "))
result=rectangle_area(l,w)
print("The area of the rectangle is: ",result,"cm^2")

#Circle area

def circle_area(radius):
    if radius<=0:
        return "\nError! Enter positive values."
    else:
        return math.pi*(radius**2)
    
r=float(input("\nEnter the radius: "))
result=circle_area(r)
print("The area of the circle is: ",result,"cm^2")

#Cylinder Volume


def cylinder_volume(radius, height):
    if radius <= 0 or height <= 0:
        return "\nError! Enter positive values."
    else:
        return math.pi * (radius**2) * height

r = float(input("Enter the radius: "))
h = float(input("Enter the height: "))

result = cylinder_volume(r, h)

print("\nThe volume of the cylinder is:", result, "cm^3")


    
    
