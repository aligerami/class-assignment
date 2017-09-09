def  q_1(s1,s2):
    return s2.find(s1) !=-1

def is_palindrom(s1):
    temp=""
    for i in s1:
        if  (ord(i)>=97 and ord(i)<=123):
            temp(i)
    return is_palindrome(temp)

def q_2(string):
    for i,char in enumerate(string):
        if char != string[-i-1]:
            return False
    return True

def q_4():
    list=eval(input("enter number like that [1,2,3,4,5]"))
    for i in list:
        for j in list:
            print( "(",i,",",j,")" , end="")
        print()
        
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


print(q_3([1,2,3,4,5,5,5,5]))

    