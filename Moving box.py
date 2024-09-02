import pgzrun
WIDTH=700
HEIGHT=700
Box=Rect((20,20),(50,50))

def draw():
    screen.clear()
    screen.draw.filled_rect(Box,"blue")
    
def update():
    Box.x=Box.x+2
    if Box.x >WIDTH:
        Box.x=0

pgzrun.go()

    




