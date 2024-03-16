def fact(number):
    if number==0 or number==1:
        return 1
    else:
        factorial=1
        for i in range(1,number+1):
            factorial*=i
        return factorial
    

# npr = n! / (n-r)! & ncr = npr / r!
    
n=int(input("Enter the value for n : "))
r=int(input("Enter the value for r : "))

npr= fact(n)/fact(n-r)
ncr= npr/fact(r)

print("npr = ",npr)
print("ncr = ",ncr)

print()
