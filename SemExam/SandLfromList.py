def min_max(list):
    small=list[0]
    large=list[0]

    #read each element from the list and compare
    for num in list[1: ]:
        
        if small>num:
            small=num
        if large<num:
            large=num

    #return smallest and largest element
    return small,large

#declare a list to store elements
elements=[]

#read no of inputs
n=int(input("Enter the no of elements : "))

print("Enter the elements : ")
for i in range(n):

    #read each element
    temp=int(input())

    #append the element into the list elements
    elements.append(temp)

#call function min_max() s,l are used to store small and large values
s,l=min_max(elements)

print("Smallest element is : ",s)
print("Largest element is : ",l)