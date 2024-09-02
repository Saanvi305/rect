import pgzrun
rect=Rect((30,30),(76,76))

WIDTH=600
HEIGHT=600
def draw():
    screen.clear()
    screen.fill ("red")
    screen.draw.line((0,0),(500,300),("red"))
    screen.draw.circle((350,350),60,("blue"))
    screen.draw.filled_circle((290,290),80,("green"))
    screen.draw.filled_rect((rect),("violet"))











pgzrun.go()