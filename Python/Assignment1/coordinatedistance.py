import math

# distance**2 = (x2-x1)**2 + (y2-y1)**2

x1=int(input("Enter value of x1: "))
x2=int(input("Enter value of x2: "))
y1=int(input("Enter value of y1: "))
y2=int(input("Enter value of y2: "))

distance=math.sqrt((x2-x1)**2+(y2-y1)**2)

print("Distance is : ",distance)

print()

Output: 

  Enter value of x1: 3
  Enter value of x2: 2
  Enter value of y1: 2
  Enter value of y2: 4
  Distance is :  2.23606797749979
