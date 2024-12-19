#Project_1.2.5_fw.py
import turtle as trtl
from turtle import Screen, Turtle
import random as rand
from random import randint

apple = "apple.gif"
strawberry = "strawberry.gif"
banana = "banana.gif"
lemon = "lemon.gif"
broccoli = "broccoli.gif"
lettuce = "lettuce.gif"
cucumber = "cucumber.gif"

screen = Screen()
screen.tracer(0)
screen.register_shape("apple.gif")
screen.register_shape("strawberry.gif")
screen.register_shape("banana.gif")
screen.register_shape("lemon.gif")
screen.register_shape("broccoli.gif")
screen.register_shape("lettuce.gif")
screen.register_shape("cucumber.gif")

start_gs = trtl.Turtle()
start_gs.hideturtle()
font_setup = trtl.Turtle()
writer = trtl.Turtle()
writer.hideturtle()
score_writer= trtl.Turtle()
counter =  trtl.Turtle()
score_block = trtl.Turtle()
apple_cover = trtl.Turtle()

apple_t = trtl.Turtle()
apple_t.speed(0)
apple_t.pencolor("#4c3732")
strawberry_t = trtl.Turtle()
orchard_t = trtl.Turtle()
orchard_t.pencolor("#4c3732")
orchard_t.fillcolor("#4c3732")
banana_t = trtl.Turtle()
lemon_t = trtl.Turtle()
broccoli_t = trtl.Turtle()
lettuce_t = trtl.Turtle()
cucumber_t = trtl.Turtle()

wn = trtl.Screen()
wn.screensize(canvwidth = 0.65, canvheight= 0.65)

#start game screen
start_gs.fillcolor("black")
start_gs.hideturtle()
start_gs.penup()
start_gs.goto(-600,-600)
start_gs.pendown()
start_gs.setheading(90)
start_gs.begin_fill()
start_gs.forward(1200)
start_gs.right(90)
start_gs.forward(1200)
start_gs.right(90)
start_gs.forward(1200)
start_gs.right(90)
start_gs.forward(1200)
start_gs.right(90)
start_gs.end_fill()
#start game text
font_setup = ("Arial", 50 , "normal")
writer.color("white")
writer.penup()
writer.goto(-415,165)
writer.write("Find the Strawberry", font=font_setup)
font_setup = ("Arial", 30 , "normal")
writer.color("red")
writer.penup()
writer.goto(-390,110)
writer.write("Press 'Space' to Start Game", font=font_setup)
font_setup = ("Arial", 50 , "normal")
writer.color("white")
writer.penup()
writer.goto(-280,300)
writer.write("Level 1", font=font_setup)

timer = 1000
counter_interval = 1   #1000 represents 1 second
timer_up = False

game_end = False

level = 1
#functions
def nextlevel():
   global level
   level = level + 1
   print(level)
   start_game()

def start_game():
   if level == 1:
       start_gs.reset()
       writer.reset()
       screen.bgpic("orchard.png")
       screen.onclick(strawberry_clicked)
       #scorescreen
       score_block.fillcolor("black")
       score_block.hideturtle()
       score_block.penup()
       score_block.goto(30,-600)
       score_block.pendown()
       score_block.setheading(90)
       score_block.begin_fill()
       score_block.forward(1200)
       score_block.right(90)
       score_block.forward(1200)
       score_block.right(90)
       score_block.forward(1200)
       score_block.right(90)
       score_block.forward(1200)
       score_block.right(90)
       score_block.end_fill()
       for i in range(150):
           apple_positions()
       strawberry_positions()
       for i in range(150):
           apple_positions()
       wn.ontimer(countdown, counter_interval)
       print("Game Started")
   if level == 2:
       wn.onkeypress(nextlevel, 'space')
       start_gs.fillcolor("black")
       start_gs.hideturtle()
       start_gs.penup()
       start_gs.goto(-600,-600)
       start_gs.pendown()
       start_gs.setheading(90)
       start_gs.begin_fill()
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.end_fill()
       #start game text
       font_setup = ("Arial", 50 , "normal")
       writer.color("white")
       writer.penup()
       writer.goto(-375,165)
       writer.write("Find the Lemon", font=font_setup)
       font_setup = ("Arial", 30 , "normal")
       writer.color("red")
       writer.penup()
       writer.goto(-390,110)
       writer.write("Press 'Space' to Start Game", font=font_setup)
       font_setup = ("Arial", 50 , "normal")
       writer.color("white")
       writer.penup()
       writer.goto(-280,300)
       writer.write("Level 2", font=font_setup)
       strawberry_t.hideturtle()
   if level == 3:
       global timer
       timer = 1000
       print("Game Started")
       screen.bgpic("orchard.png")
       screen.onclick(lemon_clicked)
       screen.update()
       start_gs.reset()
       writer.reset()
       for i in range(250):
           banana_positions()
       lemon_positions()
       for i in range(300):
           banana_positions()
       global game_end
       game_end = False
       wn.ontimer(countdown, counter_interval)
   if level == 4:
       wn.onkeypress(nextlevel, 'space')
       start_gs.fillcolor("black")
       start_gs.hideturtle()
       start_gs.penup()
       start_gs.goto(-600,-600)
       start_gs.pendown()
       start_gs.setheading(90)
       start_gs.begin_fill()
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.forward(1200)
       start_gs.right(90)
       start_gs.end_fill()
       #start game text
       font_setup = ("Arial", 50 , "normal")
       writer.color("white")
       writer.penup()
       writer.goto(-405,165)
       writer.write("Find the Cucumber", font=font_setup)
       font_setup = ("Arial", 30 , "normal")
       writer.color("red")
       writer.penup()
       writer.goto(-390,110)
       writer.write("Press 'Space' to Start Game", font=font_setup)
       font_setup = ("Arial", 50 , "normal")
       writer.color("white")
       writer.penup()
       writer.goto(-280,300)
       writer.write("Level 3", font=font_setup)
       lemon_t.hideturtle()
   if level == 5:
       timer = 1000
       print("Game Started")
       screen.bgpic("orchard.png")
       screen.onclick(cucumber_clicked)
       screen.update()
       start_gs.reset()
       writer.reset()
       for i in range(150):
           broccoli_positions()
           lettuce_positions()
       cucumber_positions()
       for i in range(200):
           broccoli_positions()
           lettuce_positions()
       game_end = False
       wn.ontimer(countdown, counter_interval)

def draw_apple():
   apple_t.shape(apple)
   #screen.update()

def draw_strawberry():
   strawberry_t.shape(strawberry)
   #screen.update()

def draw_banana():
   banana_t.shape(banana)
   #screen.update()

def draw_lemon():
   lemon_t.shape(lemon)
   #screen.update()

def draw_broccoli():
   broccoli_t.shape(broccoli)
   #screen.update()

def draw_lettuce():
   lettuce_t.shape(lettuce)
   #screen.update()

def draw_cucumber():
   cucumber_t.shape(cucumber)
   #screen.update()

def apple_positions():
   global apple_amount
   apple_amount = 0
   if apple_amount <= 1:
       apple_t.hideturtle()
       apple_t.penup()
       apple_t.goto(0,0)
       apple_t.goto(randint(-550,0),randint(-150,550))
       apple_t.stamp()
       draw_apple()


       apple_amount = apple_amount + 1


def banana_positions():
   global banana_amount
   banana_amount = 0
   if banana_amount <= 1:
       banana_t.hideturtle()
       banana_t.penup()
       banana_t.goto(0,0)
       banana_t.goto(randint(-550,0),randint(-150,550))
       banana_t.stamp()
       draw_banana()


       banana_amount = banana_amount + 1


def broccoli_positions():
   global broccoli_amount
   broccoli_amount = 0
   if broccoli_amount <= 1:
       broccoli_t.hideturtle()
       broccoli_t.penup()
       broccoli_t.goto(0,0)
       broccoli_t.goto(randint(-550,0),randint(-150,550))
       broccoli_t.stamp()
       draw_broccoli()


       broccoli_amount = broccoli_amount + 1


def lettuce_positions():
   global lettuce_amount
   lettuce_amount = 0
   if lettuce_amount <= 1:
       lettuce_t.hideturtle()
       lettuce_t.penup()
       lettuce_t.goto(0,0)
       lettuce_t.goto(randint(-550,0),randint(-150,550))
       lettuce_t.stamp()
       draw_lettuce()


       lettuce_amount = lettuce_amount + 1


x = randint(-550,0)
y = randint(-150,550)
def strawberry_positions():
   strawberry_t.penup()
   strawberry_t.goto(0,0)
   strawberry_t.goto(x,y)
   strawberry_t.stamp()
   draw_strawberry()
   strawberry_t.stamp()


def strawberry_clicked(x,y):
   global game_end
   if strawberry_t.distance(x, y) < 50:
       print("Strawberry Found!")
       game_end = True
       apple_t.clear()
       apple_t.hideturtle()
       strawberry_t.clear()
       screen.update()
       global level
       level = level + 1


x2 = randint(-550,0)
y2 = randint(-150,550)
def lemon_positions():
   lemon_t.penup()
   lemon_t.goto(0,0)
   lemon_t.goto(x2,y2)
   lemon_t.stamp()
   draw_lemon()
   lemon_t.stamp()


def lemon_clicked(x2,y2):
   global game_end
   if lemon_t.distance(x2, y2) < 50:
       print("Lemon Found!")
       game_end = True
       banana_t.clear()
       banana_t.hideturtle()
       lemon_t.clear()
       screen.update()
       global level
       #level = level + 1


x3 = randint(-550,0)
y3 = randint(-150,550)
def cucumber_positions():
   cucumber_t.penup()
   cucumber_t.goto(0,0)
   cucumber_t.goto(x3,y3)
   cucumber_t.stamp()
   draw_cucumber()
   cucumber_t.stamp()


def cucumber_clicked(x3,y3):
   global game_end
   if cucumber_t.distance(x3, y3) < 50:
       print("Cucumber Found!")
       game_end = True
       broccoli_t.clear()
       broccoli_t.hideturtle()
       lettuce_t.clear()
       lettuce_t.hideturtle()
       cucumber_t.clear()
       screen.update()
       global level
       level = level + 1


def countdown():
 global timer, timer_up
 counter.clear()
 if timer <= 0:
   global font_setup
   counter.write("You Lose", font=font_setup)
   timer_up = True
   broccoli_t.clear()
   broccoli_t.hideturtle()
   lettuce_t.clear()
   lettuce_t.hideturtle()
   banana_t.clear()
   banana_t.hideturtle()
   apple_t.clear()
   apple_t.hideturtle()
 else:
   font_setup = ("Arial", 20 , "bold")
   counter.color("white")
   counter.hideturtle()
   counter.goto(45,475 )
   counter.write("Score: " + str(timer), font=font_setup)
   timer -= 1
   if game_end == False:
       counter.getscreen().ontimer(countdown, counter_interval)
   if game_end == True:
      global score_amount
      score_amount = timer + 1
      addscore()
      print(sum(score))
      return None
 
score = []


def addscore():
   score.append(score_amount)
   print(score)


#screen.tracer(True)


wn.onkeypress(start_game, 'space')
wn.listen()
screen.mainloop()