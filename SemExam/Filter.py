

#without using lambda
def ispos(x):
    return x>0
    
n=int(input("Enter the no of terms : "))
numbers=[]

for i in range(n):
    numbers+=[int(input("Enter : "))]
    
filter_values= filter(ispos, numbers)
pos_val= list(filter_values)
print(pos_val)

#using lambda

positivenum=list(filter(lambda x:x>0,numbers))
print(positivenum)
