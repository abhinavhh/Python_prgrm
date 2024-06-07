string = input("Enter a string: ")
distance = int(input("Enter a distance value : "))
code = ""
for ch in string:
    ordvalue = ord(ch)
    cyphervalue = ordvalue - distance
    if cyphervalue < ord('a'):
        cyphervalue = ord('z') - \
            (distance - (ord('a') - ordvalue - 1))
    code += chr(cyphervalue)
print(code)
print()