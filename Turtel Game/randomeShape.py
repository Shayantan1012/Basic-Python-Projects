from turtle import Turtle
tim= Turtle()
import random
colors=['peru','deep pink',"CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def drawShape(num_sides):
    angle=360/num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        tim.speed(3)
        
        
        
for shape_side_n in range(1, 10):
    tim.color(random.choice(colors))
    tim.fillcolor(random.choice(colors))
    drawShape(shape_side_n)        
   
   
    