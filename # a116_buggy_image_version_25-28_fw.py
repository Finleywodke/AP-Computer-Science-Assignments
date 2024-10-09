#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as spider,
# a less useful variable name x is used

# creates the spider body (10-12)
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
# configures leg amount and leg length as well as the angle of the legs
legs = 8
leg_length = 100
angle = 360 / legs
spider.pensize(5)
numLegDrawn = 0
# the while loop draws the spider
while (numLegDrawn < legs):
  spider.goto(0,20)
  spider.setheading(angle*numLegDrawn)
  spider.forward(leg_length)
  numLegDrawn = numLegDrawn + 1
spider.hideturtle() 
wn = trtl.Screen()
wn.mainloop()