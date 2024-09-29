import pgzrun
import random 

WIDTH = 600
HEIGHT= 600

bee=Actor("bee.png")
flower=Actor("flower.png")
bee.x= 200
bee.y=400
def draw():
    screen.blit("bg")
    bee.draw()
    flower.draw()



pgzrun.go()
