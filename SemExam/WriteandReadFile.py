file=open("./file.txt",'w')
file.write("Programming in python")
print("write successfull")
file.close()


f2=open("./file.txt",'r')
content=f2.read()
print(content)
f2.close()