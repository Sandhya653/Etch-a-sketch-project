#AIM
"""
W - Forwards
S - Backwards
A -counterclockwise #leftwords
D -clockwise #rightwards
c -clear
"""
from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()
list=["w","s","a","d","c"]


def on_click_forward():
    tim.forward(90)
screen.listen()
screen.onkey(key="w",fun=on_click_forward)



def on_click_backward():
    tim.backward(90)
screen.onkey(key="s",fun=on_click_backward)



def on_click_counterclockwise():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)
screen.onkey(key="a",fun=on_click_counterclockwise)



def on_click_clockwise():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
screen.onkey(key="d",fun=on_click_clockwise)

#Alternative Method
"""def on_click_clockwise():
    tim.right(45)
    tim.setheading(0)

screen.onkey(key="d",fun=on_click_clockwise)
"""


def on_click_clear():
    tim.clear()
    tim.penup()
    tim.home()
screen.onkey(key="c",fun=on_click_clear)
screen.exitonclick()