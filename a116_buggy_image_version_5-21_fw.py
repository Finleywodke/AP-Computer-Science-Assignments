#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as spider,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 6
leg_length = 200
angle = 380 / legs
spider.pensize(5)
numLegDrawn = 0
while (numLegDrawn < legs):
  spider.goto(0,0)
  spider.setheading(angle*numLegDrawn)
  spider.forward(leg_length)
  numLegDrawn = numLegDrawn + 1
spider.hideturtle() 
wn = trtl.Screen()
wn.mainloop()