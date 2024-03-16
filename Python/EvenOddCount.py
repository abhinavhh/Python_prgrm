totalElements=int(input("Enter the total no of elements : "))
elements=[]#List to store the values
for i in range (totalElements):
    addToList=int(input())#read elements
    elements.append(addToList)#add elements to the list
evencount=0
for i in (elements):
    if i%2 == 0 :
        evencount=evencount+1
oddcount=totalElements-evencount
print("Even count is ",evencount)
print("Odd count is ",oddcount)
print()