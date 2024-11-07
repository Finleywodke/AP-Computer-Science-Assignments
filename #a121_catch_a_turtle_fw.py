#a121_catch_a_turtle_fw.py

#-----import statements-----
import turtle as trtl
import random as rand

#-----initialize turtle-----
t= trtl.Turtle()
score_writer= trtl.Turtle()
counter =  trtl.Turtle()

#-----game configuration----

t.hideturtle()
t.pencolor("black")
t.fillcolor("red")
t.pensize(20)
t.shape("circle")
t.shapesize(3)

font_setup = ("Arial", 40 , "normal")

score_writer.hideturtle()
score_writer.pencolor("black")
score_writer.pensize(10)
score_writer.penup()
score_writer.goto(-300,275)
score_writer.pendown()

counter.hideturtle()
counter.penup()
counter.goto(150,275)
counter.pendown()

score = 0

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----game functions--------
def t_clicked(x,y):
    change_position()

def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,150)
    t.hideturtle()
    t.penup()
    t.goto(new_xpos,new_ypos)
    t.pendown()
    t.showturtle()
    update_score()

def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font= font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    t.hideturtle()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----events----------------
t.onclick(t_clicked)
wn = trtl.Screen()
wn.bgcolor("#B5A894")
wn.ontimer(countdown, counter_interval) 
t.showturtle()
wn.mainloop() 