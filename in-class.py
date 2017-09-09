def  q_1(s1,s2):
    return s2.find(s1) !=-1

def q_2(s1):
    temp=""
    for i in s1:
        if  (ord(i)>=97 and ord(i)<=123):
            temp(i)
    return is_palindrome(temp)

def is_palindrome(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

def q_3(list):
    temp=[]
    flag=True
    for i in list:
        for j in temp:
            if i==j:
                flag=False
        if flag==True:
            temp.append(i)
            
        flag=True
    return temp

def q_4():
    list=eval(input("enter number like that [1,2,3,4,5]"))
    for i in list:
        for j in list:
            print( "(",i,",",j,")" , end="")
        print()
        



print(q_3([1,2,3,4,5,5,5,5]))


string1 = input("Enter a string: ")
cha = input("Enter a charactor: ")


def checkCharacter (s1, char):
    if char in s1:
        if s1.count(char) == 1:
            return True
        else:
            return False
    else:
        return False
if checkCharacter(string1,cha):
    print ("This string contains the charactor and has no duplicate charactor value.")
else:
    print("It doesn\'t meet the requirement.")

import random

matrix = []
num = eval(input("Enter the number:"))


for row in range(0, num):
    matrix.append([])
    for columns in range(0, num):
        matrix[row].append(random.randint(0,1))
print(matrix)

result=1
for i in range(num):
    for j in range(num):
        if i == j:
            result=matrix[i][j] *result
                
print ("The matrix is diagonal matrix:",end = '')
print(result!=0)
    