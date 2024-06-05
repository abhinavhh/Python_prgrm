file=open("./file.txt",'r')
count=0
for line in file:
    words=line.split()
    for word in words:
        if len(word)==4:
            count+=1
print(count)

# f2=open("./file.txt",'w')
# f2.write("Hel")