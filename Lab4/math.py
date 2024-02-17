# task 1
import math
x = float(input("Input degree: "))
y = x*math.pi/180
print("Output radian: ",y)

#--------------------------------------------------

# task 2
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

print("Expected Output: ",(a + b)/2*h)

#--------------------------------------------------


# task 3
import math
n = float(input("Input number of sides: "))
x = float(input("Input the length of a side: "))

t = x**2*math.sqrt(3)/4

print("The area of the polygon is: ",t*4)

#--------------------------------------------------

# task 4
a = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

S = a*h
print("Expected Output: ",S)

