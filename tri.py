import turtle

def draw_triangle(some_turtle):
    for i in range(1,4):
        some_turtle.backward(100)
        some_turtle.right(60)
        some_turtle.right(60)

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.backward(100)
        some_turtle.left(90)
        
        
def draw_art():        
    window = turtle.Screen()
    window.bgcolor("yellow")
    
 #create turtle brad- draw a square   
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    for i in range(1,2):
        draw_triangle(brad)
       # brad.right(10)

   
    diva = turtle.Turtle()
    diva.shape("arrow")
    diva.color("green")
    diva.speed(2)
    for i in range(1,2):
      draw_square(diva)
    

    window.exitonclick()

draw_art()
