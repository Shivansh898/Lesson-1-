import pgzrun
WIDTH = 800
HEIGHT = 525

def draw():
    screen.fill("white")  
    R = 250
    C = ["black","blue", "red", "yellow"]
    for i in range(4):  
        screen.draw.filled_circle((400,262.5),R,C[i])
        R = R -60
pgzrun.go()