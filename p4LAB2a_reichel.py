import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(4)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced 

for i in [0,1,2,3]:
    t.forward(50)
    t.left(90)

for i in [0,1,2]:
    t.forward(100)
    t.left(120)


# end commands
win.mainloop()             # Wait for user to close window
