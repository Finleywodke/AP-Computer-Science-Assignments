#   a118_turtles_in_traffic_fw.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

wn = trtl.Screen()
wn.screensize(canvwidth = 0.65, canvheight= 0.65)

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

    #tutrles on top of screen
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

    #turtles on the left side of the screen
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)

  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

speedx = 10
speedy = 9

for step in range(100):
   
    for ht in horiz_turtles:
        ht.forward(50 + speedx)
    if (abs(ht.xcor() - vt.xcor()) < 5):
        vert_turtles.remove(vt)
        vt.right(360)
  
    for vt in vert_turtles:
        vt.forward(50 + speedy)
    if (abs(ht.ycor() - vt.ycor()) < 5):
         horiz_turtles.remove(ht) 
         ht.left(360)

    speedx =+ 2
    speedy =+ 3

    step = step + 3

wn.mainloop()