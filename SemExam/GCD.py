def gcd(a,b):
    if b==0:
        #base case if b==0 then gcd(b,a)=a
        return a
    
    return gcd(b,a%b)
num1=int(input("Enter the value  of first num"))
num2=int(input("Enter the value of second num"))
print(f"GCD of {num1} and {num2} is : {gcd(num1,num2)}")
print()