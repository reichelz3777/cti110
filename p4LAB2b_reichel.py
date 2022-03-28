import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced 

t.forward(100)          
t.right(135)            
t.forward(120)
t.left(135)
t.forward(100)

t.penup()
t.forward(50)
t.pendown()

t.left(90)
t.forward(90)
t.right(90)
t.forward(75)
t.right(145)
t.forward(90)
t.left(115)
t.forward(75)

# end commands
win.mainloop()             # Wait for user to close window
