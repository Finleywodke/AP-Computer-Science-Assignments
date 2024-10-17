#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic","arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold","red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  
startx = 0
starty = 0
angle = 0
moveforward = 5

#
for t in my_turtles:
  t.speed(100)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(45)  
  t.setheading(angle + 45)   
  t.forward(moveforward)
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)
  angle = t.heading()
  moveforward = moveforward + 5

#	
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()