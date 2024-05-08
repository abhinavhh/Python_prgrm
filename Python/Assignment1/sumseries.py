
#series is 1/1 + 1/2 + 1/3 + .......... 1/n

n=int(input("Enter the no  of terms : "))
sum=0.0

#calculating sum of n terms of the series 

for i in range(1,n+1):
    sum+=1/i
print(sum)
print()

Output : 

    Enter the no  of terms : 6
    2.4499999999999997
