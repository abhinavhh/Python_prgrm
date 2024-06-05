#read a string from user 
string=input("Enter a string : ")

#declare a empty dictionary to store each character with its count
char_count={}

for char in string:

    #element already added to the dictionary
    if char in char_count:
        char_count[char]+=1

    #element which is not yet been added
    else:
        char_count[char]=1
print(char_count)

#sample output for string "HELLO"

# o/p---> {'h':1 ,'e':1 ,'l':2 ,'o':1}