import turtle

def draw_circle():

     window = turtle.Screen()
     window.bgcolor("green")

     flower = turtle.Turtle()
     flower.shape("arrow")
     flower.color("red")
     flower.speed(2)
     

     flower.circle(100)
     flower.right(360/30)
     flower.circle(100)

     for i in range(0,20,4):
       draw_circle(flower)

     window.exitonclick()

draw_circle()
