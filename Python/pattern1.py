#pattern is          A
#                   A B
#                  A B C
#                 A B C D

rows=int(input("Enter the no of rows (greater than 0 && Less than 27): "))#reading number of rows to print
num=rows #num is used for controling space printing loop
if rows>0 and rows<=26:
    for i in range(1,rows+1):
        start=65
        for j in range(num):
            print("",end=" ")#print  space to center the row
        num-=1
        for k in range(i):
            char=chr(start)
            print(char,end=" ")
            start+=1
        print()#next row