import math

print("------ax**2+bx+c=0-------")


a=int(input("enter value for a : "))
b=int(input("enter value for b : "))
c=int(input("enter value for c : "))

#(-b +- sqrt(b**2 - 4*a*c)) / 2*a  is the equation

d=b**2-4*a*c

solution1=(-b+math.sqrt(d))/2
solution2=(-b-math.sqrt(d))/2

if solution1==solution2:
    print("Solution is : ",solution1)
else:
    print("Solution is : ",solution2)
    print("Solution is : ",solution1)

print()
