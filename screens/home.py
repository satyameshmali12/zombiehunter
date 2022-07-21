# creating the home screen it will be further used in the main.py where the main game is running
import pygame

# bringing all the function from the resources folder
from resources.functions import loadimage,displayimage,displaytext,scaleimage,listallthefiles

# width and height of the screen

width = 1200
height = 700

background = scaleimage(loadimage("sprites/back/ground.jpg"),1200,700)

# loading all the images of the male and female zombie :-state idle
zombiefrun = listallthefiles("sprites/zombie/female/walk")
zombiemrun  = listallthefiles("sprites/zombie/male/idle")


# all the home code here👇

k = "j"

def home(display,zombiecount,zombie1x,zombie2x):
    pygame.display.set_caption("Home")
    display.fill("blue")

    # print(k)

    displayimage(display,background,0,0)
    
    if zombiecount == len(zombiefrun):
        zombiecount=0

    displayimage(display,scaleimage(zombiefrun[zombiecount],229,250),zombie1x,height-300)

    # flipping->transforming->displaying the image
    displayimage(display,pygame.transform.flip(scaleimage(zombiemrun[zombiecount],229,250),True,False),zombie2x,100)
    # displayimage(display,pygame.transform.flip(),100,140),300,100)
    
    return zombiecount+1,zombie1x+1,zombie2x+1
    