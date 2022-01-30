from graphics import *
win = GraphWin()
hello = "hello"
corna = float(input())
cornb = float(input())
side = float(input())
for i in range(100):
    for j in range(100):
       x = corna+i*(side/100)
       y = cornb+j*(side/100)
       c = int((x**2)+(y**2))
       if (c % 2) == 0:
           print(c)
           pt = Point(i, j)
           pt.draw(win)
while hello != "finished":
    hello = input("finished?")