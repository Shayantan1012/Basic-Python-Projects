import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
screen = t.Screen()

screen.setup(width=1.0, height=1.0) 

tim.goto(0, 0)
def fillColor():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    return (r,g,b)
    
tim.right(230)
for _ in range(200):
   # tim.color(random.choice(colours))
    tim.forward(50)
    tim.setheading(random.choice(directions))
    tim.pencolor(fillColor())

screen.exitonclick()  