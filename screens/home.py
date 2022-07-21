# creating the home screen it will be further used in the main.py where the main game is running
from turtle import speed
import pygame

# bringing all the function from the resources folder
from resources.functions import loadimage,displayimage,displaytext,scaleimage,listallthefiles

# width and height of the screen

width = 1200
height = 700

background = scaleimage(loadimage("sprites/back/ground.jpg"),1200,700)

# loading all the images of the male and female zombie :-state idle
zombiefrun = listallthefiles("sprites/zombie/female/walk")
zombiemrun  = listallthefiles("sprites/zombie/male/walk")


# all the home code here👇

k = "j"

def home(display,zombiecount,zombie1x,zombie2x):
    zombie1xspeed = 3
    zombie2xspeed = -3

    # if zombie1x
    pygame.display.set_caption("Home")
    display.fill("blue")

    # print(k)

    displayimage(display,background,0,0)
    
    if zombiecount == len(zombiefrun):
        zombiecount=0

    # if zombie1
    # if speed = 3
    displayimage(display,scaleimage(zombiefrun[zombiecount],229,250),zombie1x,height-300)

    # flipping->transforming->displaying the image
    displayimage(display,pygame.transform.flip(scaleimage(zombiemrun[zombiecount],229,250),True,False),zombie2x,height-300)
    
    return zombiecount+1,zombie1x+zombie1xspeed,zombie2x+zombie2xspeed
    