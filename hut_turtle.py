import turtle
t = turtle.Turtle()
#s = turtle.getscreen()
bg='blue4'
turtle.bgcolor(bg)
t.speed(5)
t.up()
t.goto(-100,100)
t.pd()
t.color('black', 'yellow')
t.begin_fill()
for i in range(2):
    t.fd(200)
    t.rt(90)
    t.fd(200)
    t.rt(90)
t.end_fill()
t.color('black', 'red')
t.begin_fill()
t.lt(45)
t.fd(140)
t.rt(90)
t.fd(140)
t.up()
t.end_fill()
t.home()
t.goto(100,-100)
t.bk(70)
t.begin_fill()
t.lt(90)
t.pd()
t.fd(100)
t.lt(90)
t.fd(60)
t.lt(90)
t.fd(100)

t.end_fill()

t.color(bg, 'white')
t.up()
t.home()
t.goto(150,260)
t.rt(180)
t.pd()
t.begin_fill()
t.circle(60)
t.end_fill()
t.color(bg,bg)
t.up()
t.home()
t.goto(180,260)
t.rt(180)
t.pd()
t.begin_fill()
t.circle(60)
t.end_fill()
t.color('green')
t.up()
t.goto(60,-100)
t.pd()
t.bk(100)
t.begin_fill()
t.lt(150)
t.fd(150)

t.rt(150)
t.fd(600)

t.rt(150)
t.fd(150)

t.rt(30)
t.fd(300)

t.end_fill()


