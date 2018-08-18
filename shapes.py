import turtle

def draw_square(some_turtle):
  for i in range(4):
    some_turtle.forward(100)
    some_turtle.right(90)

def draw_triangle(some_turtle):
  for i in range(4):
    some_turtle.forward(100)
    some_turtle.right(120)

def draw_art(): 
  window = turtle.Screen()
  window.bgcolor("white")

  brad = turtle.Turtle()
  brad.shape("turtle")
  brad.color("green")
  brad.speed(20)

  for i in range(72):
    draw_square(brad)
    # brad.circle(50)
    # draw_triangle(brad)
    brad.right(5)
  
  window.exitonclick()

draw_art()