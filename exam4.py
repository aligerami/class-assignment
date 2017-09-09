
number = int(input("Enter an integer from 1 to 15: "))
#number=7
temp=0
for i in range (1,number+1):
    
    for j in range (number-i,0,-1):
        print("  ",end="")
        
    for j in range (1,i):
        print (j,end=" ")
    for h in range (i,0,-1): 
        print(h,end=" ")   
    print(" ")


