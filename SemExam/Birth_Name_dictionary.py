n=int(input("Enter the no of entries : "))
birth_name={}
for i in range(n):
    name=input("Enter name : ")
    date=input("Enter Birth Date : ")
    birth_name[name]=date
s=input("Enter the name of a person : ")
if s in birth_name:
    print(birth_name[s])
else:
    print("Name not Found..")
