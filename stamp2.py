import turtle

turtle.setup(width=600, height=600) #창 크기 600x600
gil=turtle.Turtle()
t=turtle.Turtle()

#길 만들기
def draw_gil() :
    gil.penup()
    gil.goto(-150,-300)
    gil.pendown()
    gil.pensize(5)
    gil.color("brown")
    gil.begin_fill()
    gil.goto(-150,300)
    gil.goto(150,300)
    gil.goto(150,-300)
    gil.goto(-150,-300)
    gil.end_fill()

#거북이 찍기
def stamp():
    xy=[[-75,-250],[50,-200],[-50,-150],[50,-100],
    [-25,50],[50,75],[-75,100],[100,150],[-50,200]] #거북이들을 찍을 좌표들
    t.shape("turtle")
    t.color("green")
    t.setheading(90) #거북이의 머리가 북쪽을 향하게 
    t.penup()
    t.goto(xy[0])
    t.stamp()
    for x,y in xy :
        t.goto(x,y)
        t.stamp()
    
#함수 실행
draw_gil()
stamp()

