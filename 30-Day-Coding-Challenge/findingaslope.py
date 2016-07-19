#This is a program on finding the slope:
#Day 2 Python Coding Challenge update 

print("This is a program to find the slope of a line that passes through points")
print("Enter points for x1,x2, y1, and y2 to find the slope")
      
 
y1 = float(raw_input("Enter y1: "))
y2 = float(input("Enter y2: "))
rise = y2 -y1

 
x1 = float(raw_input("Enter x1:"))
x2 = float(raw_input("Enter x2: "))
run = x2 - x1

 
m = rise/run
print ("The slope will be: ", m)
