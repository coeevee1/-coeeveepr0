x = float(input())
if (x == int):
    x = int(input())
Estop = 2

import turtle

t = turtle.Turtle()

for c in ['red', 'green', 'yellow', 'blue']:
    for (i) in range(Estop):
        t.speed(100)
        t.circle(x, x)
        t.left(x)
        t.forward(x)
        t.penup
        t.circle(x, x)
        t.left(x)
        t.pendown
        t.right(x)
        t.forward(x)
        t.forward(x)
        t.right(x)
        t.circle(x, x)
        t.right(x)
        t.forward(x)
        t.left(x)
        t.circle(x, x)
        t.forward(x)
        t.circle(x, x)
        t.left(x)
        t.forward(x)
        t.speed(100)
        t.right(x)
        t.forward(x)
        t.forward(x)
        t.right(x)
        t.circle(x, x)
        t.right(x)
        t.forward(x)
        t.left(x)
        t.circle(x, x)
        t.forward(x)
        t.circle(x, x)
        t.left(x)
        t.forward(x)
        t.right(x)
        t.forward(x)
        t.forward(x)
        t.right(x)
        t.circle(x, x)
        t.right(x)
        t.forward(x)
        t.left(x)
        t.circle(x, x)
        t.forward(x)
        t.circle(x)
        Estop = Estop - 1
        if Estop == 1:
                print("would you like to continue if so enter how many times")
                Estop = int(input())
                if (Estop == float):
                    Estop = float(input())