import pgzrun
WIDTH = 800
HEIGHT = 525

def draw():
    screen.fill("white")
    screen.draw.filled_circle((400,262.5),200,"black")
    screen.draw.filled_circle((400,262.5),198,"yellow")
    screen.draw.filled_circle((400,250),160,"black")
    screen.draw.filled_circle((400,225),160,"yellow")
    screen.draw.filled_circle((312.5,182.5),20,"black")
    screen.draw.filled_circle((487.5,182.5),20,"black")

pgzrun.go()