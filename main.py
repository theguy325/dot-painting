import colorgram, turtle, random
colors = colorgram.extract("image.jpeg", 20)
rgb_color = []
turtle.colormode(255)
tate = turtle.Turtle()
tate.hideturtle()
tate.penup()
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    rgb_color.append(color_tuple)
tate.setheading(225)
tate.forward(300)
tate.setheading(0)
for dot_count in range(1, 101):
    tate.dot(20, random.choice(rgb_color))
    tate.forward(50)
    if dot_count % 10 == 0:
        tate.setheading(90)
        tate.forward(50)
        tate.setheading(180)
        tate.forward(500)
        tate.setheading(0)



screen = turtle.Screen()
screen.exitonclick()


