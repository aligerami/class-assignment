import turtle
x=int(input("Enter X :"))
y=int(input("Enter y :"))

myPen = turtle.Turtle()  
myPen.hideturtle()     
myPen.penup()
myPen.goto(-30,-25)
myPen.pendown()
myPen.forward(60)
myPen.right(-90)
myPen.forward(50)
myPen.right(-90)
myPen.forward(60)
myPen.right(-90)
myPen.forward(50)
myPen.penup()
myPen.goto(x,y)
myPen.dot(2)
myPen.penup()
myPen.goto(-30,30)
myPen.pendown()
flag=False
if (-30<x and x<30):
    if (-25<y and y<25):
        flag=True

if flag:

    myPen.write("coordinator is inside")
    
else:   
    myPen.write("coordinator is outside")
    print("coordinator is outside")
myPen.penup()
myPen.goto(1000,1000)
          
turtle.exitonclick()
