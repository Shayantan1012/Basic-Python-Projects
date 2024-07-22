from turtle import Turtle,Screen
screen=Screen()
import random
screen.setup(width=500,height=400)
all_turtle=[]

user_bed=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_count in range (0,6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_count])
    new_turtle.goto(x=-230,y=y_positions[turtle_count])
    all_turtle.append(new_turtle)


if user_bed:
    is_race_on=True

while is_race_on:
  for turtle in all_turtle:
      if(turtle.xcor()>230):
          is_race_on=False
          winning_color=turtle.pencolor()
          if(winning_color==user_bed):
                print(f"You've won! The {winning_color} turtle is the winner!")
          else:
             print(f"You've lost! The {winning_color} turtle is the winner!")
      turtle.forward(random.randint(0,10))
          
    
screen.exitonclick()



