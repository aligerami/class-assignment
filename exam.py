string=input("please enter the letter")
new_string=""
for i in string:
     i = ord(i) - 32
     new_string = new_string + chr(i)    
print(new_string)

