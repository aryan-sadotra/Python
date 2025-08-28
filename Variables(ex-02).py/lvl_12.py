#. The radius of a circle is 30 meters.
#(i) Calculate the area of a circle and assign the value to a variable name of area_of_circle
#(ii) Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#(iii) Take radius as user input and calculate the area.

r = 30
area_of_circle = 22/7 * r * r
circumference_of_circle = 2 * 22/7 * r 
print("area_of_circle: ",area_of_circle)
print("circumference_of_circle: ",circumference_of_circle)

a = int(input("Enter the radius: "))
area_of_circle = 22/7 * a * a
circumference_of_circle = 2 * 22/7 * a
print("area_of_circle: ",area_of_circle)
print("circumference_of_circle: ",circumference_of_circle)

'''
# another way 
import math

# (i) & (ii) with fixed radius
r = 30
area_of_circle = math.pi * r ** 2
circum_of_circle = 2 * math.pi * r
print("Area of circle:", round(area_of_circle, 2))
print("Circumference of circle:", round(circum_of_circle, 2))

# (iii) With user input
a = float(input("\nEnter the radius: "))
area_of_circle = math.pi * a ** 2
circum_of_circle = 2 * math.pi * a
print("Area of circle:", round(area_of_circle, 2))
print("Circumference of circle:", round(circum_of_circle, 2))

'''