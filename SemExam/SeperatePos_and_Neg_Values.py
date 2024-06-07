#Decalre a list to store negative and posiive values
list=[]

#read no of terms
n=int(input("Enter the no of elements : "))
print("Enter the elements : ")

#add element into the list
for i in range(n):
    temp=int(input())
    list.append(temp)

#declare two lists to seperate negative and positive values
pos_list=[]
neg_list=[]

for i in list:
    if i<0: 
        #append the -ve value to the list
        neg_list+=[i]
    else:
        #append the +ve value to the list
        pos_list+=[i]
print(pos_list,neg_list)