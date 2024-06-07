file=open("./median.txt",'r')
content=file.read()#read entire contents of the file
file.close()

#split strings into numbers based on whitespace and new line
numbers=[int(num)for num in content.split()]

print(numbers)
#sort the list
numbers.sort()
n = len(numbers)
mid = n // 2
    
if n % 2 == 0:
        # If even, return the average of the middle two numbers
    print((numbers[mid - 1] + numbers[mid]) / 2)
else:
        # If odd, return the middle number
   print(numbers[mid])
    
