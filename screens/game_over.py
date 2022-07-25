# creating the game_over screen it will be further used in the main.py where the main game is running
import pygame
import sys
from resources.functions import displayimage,displaytext,scaleimage

width = 1200
height = 700
homebutton = pygame.transform.scale(pygame.image.load("sprites/gui/home (2).png"),(100,100))
homebuttonx = 350
homebuttony = height/2+60

reloadbutton = pygame.transform.scale(pygame.image.load("sprites/gui/reload (2).png"),(100,100))
reloadbuttonx = 550
reloadbuttony = height/2+60

exitbutton = pygame.transform.scale(pygame.image.load("sprites/gui/exit (2).png"),(100,100))
exitbuttonx = 750
exitbuttony = height/2+60

background = pygame.transform.scale(pygame.image.load("sprites/back/background.webp"),(width,height))


def game_over(display,score,place,restart):

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0]>homebuttonx and pos[0]<homebuttonx+homebutton.get_width() and pos[1]>homebuttony and pos[1]<homebuttony+homebutton.get_height():
                place="home"
                print("you pressed home button")

            if pos[0]>reloadbuttonx and pos[0]<reloadbuttonx+reloadbutton.get_width() and pos[1]>reloadbuttony and pos[1]<reloadbuttony+reloadbutton.get_height():
                # print("you pressed reoloadbutton button")
                restart=True

            if pos[0]>exitbuttonx and pos[0]<exitbuttonx+exitbutton.get_width() and pos[1]>exitbuttony and pos[1]<exitbuttony+exitbutton.get_height():
                sys.exit()

    display.fill("purple")
    displayimage(display,background,0,0)
    displaytext(display,"Well Played" if score>0 else "Good",width/2-homebutton.get_width()-40,100,70,"black",True,True)
    displaytext(display,f"No of kills:- {score}",500,height/2-50,40,"black",True,False)

    displayimage(display,homebutton,homebuttonx,homebuttony)
    displayimage(display,reloadbutton,reloadbuttonx,reloadbuttony)
    displayimage(display,exitbutton,exitbuttonx,exitbuttony)

    return place,restart
    