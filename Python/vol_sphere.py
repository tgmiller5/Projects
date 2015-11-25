import math

def vol(r):
   return (4.0/3.0)*(math.pi)*(r**3)
my_vol = float(raw_input(“Enter a number: ”))

print “The volume of the sphere is ”, vol(my_vol)
