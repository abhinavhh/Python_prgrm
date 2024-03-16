# X**Y 

x=int(input("Enter the base : "))
y=int(input("Enter the exponent: "))

result=1
while y!=0:
    result*=x
    y-=1
print(result)
print()
