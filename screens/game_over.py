# creating the game_over screen it will be further used in the main.py where the main game is running
import pygame
import sys
from resources.functions import displayimage,displaytext,scaleimage,checkwhetherbuttonpressed

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
    
    pygame.display.set_caption("Zombie Hunter - Game Over")
    
    pygame.mixer.music.stop()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            place = checkwhetherbuttonpressed(homebutton,homebuttonx,homebuttony,pos[0],pos[1],"home","game_over")

            # due to some errors
            if place==None:
                place="game_over"

            restart = checkwhetherbuttonpressed(reloadbutton,reloadbuttonx,reloadbuttony,pos[0],pos[1],True,False)

            if pos[0]>exitbuttonx and pos[0]<exitbuttonx+exitbutton.get_width() and pos[1]>exitbuttony and pos[1]<exitbuttony+exitbutton.get_height():
                sys.exit()

    # displaying all the stuff to the gameoverscreen

    display.fill("white")
    displayimage(display,background,0,0)
    displaytext(display,"Well Played" if score>0 else "Good",width/2-homebutton.get_width()-40,100,70,"black",True,True)
    displaytext(display,f"No of kills:- {score}",500,height/2-50,40,"black",True,False)

    displayimage(display,homebutton,homebuttonx,homebuttony)
    displayimage(display,reloadbutton,reloadbuttonx,reloadbuttony)
    displayimage(display,exitbutton,exitbuttonx,exitbuttony)

    return place,restart
    