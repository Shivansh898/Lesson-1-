import pgzrun
WIDTH = 800
HEIGHT = 525

def draw():
    screen.fill("light blue")  
    W = 775
    H = 150
    for i in range(35):  
        R = Rect((100,100),(W,H))
        R.center = (400,262.5)
        screen.draw.rect(R,"purple")
        W = W-10
        H = H+10
        #screen.draw.filled_rect(R,"red")
    screen.draw.filled_circle((100,100),100,"green")
pgzrun.go()