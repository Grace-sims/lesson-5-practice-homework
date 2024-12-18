import turtle as t

t.width (9)
t.speed (0)

#circle blue
t.penup ()
t.goto (-200,80)
t.pendown ()

t.color ("#2e7fdb")
t.setheading (0)
t.circle (60)

#circle black
t.penup ()
t.goto (-60,80)
t.pendown ()

t.color ("#000000")
t.setheading (0)
t.circle (60)

#circle red
t.penup ()
t.goto (80,80)
t.pendown ()

t.color ("#ff051e")
t.setheading (0)
t.circle (60)

#circle yellow
t.penup ()
t.goto (-130,10)
t.pendown ()

t.color ("#e3b21e")
t.setheading (0)
t.circle (60)

#circle green
t.penup ()
t.goto (10,10)
t.pendown ()

t.color ("#23ad58")
t.setheading (0)
t.circle (60)

t.mainloop ()