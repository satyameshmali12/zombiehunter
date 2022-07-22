# creating the playing screen it will be further used in the main.py where the main game is running
import pygame
import sys
from resources.functions import playmusic,displayimage,displaytext,listallthefiles,scaleimage

width = 1200
height = 700

background = pygame.transform.scale(pygame.image.load("sprites/back/background.jpg"),(width,height))

location = "sprites/ninja"


# all the move

moves = ["idle","attack","glide","jump","dead","run","throwrode","slide"]

moves2 = {}

# appending all the moves to the obj 
for i in range(len(moves)):
    moves2.__setitem__(moves[i],listallthefiles(f"{location}/{moves[i]}"))


def playing(display,player,currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        playerxspeed=10
        currentmove = "run"
        direction=1
    elif keys[pygame.K_LEFT]:
        playerxspeed=-10
        currentmove = "run"
        direction=0
    else:
        playerxspeed=0
        currentmove = "idle"
    

    if movecount==len(moves2[currentmove]):
        movecount=0
    if not pygame.mixer.music.get_busy():
        playmusic("audio/zombiegroup.mp3")
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            sys.exit()

    display.fill("white")

    displayimage(display,background,0,0)

    # displaying the character over here

    if direction==0:
        displayimage(display,pygame.transform.flip(scaleimage(moves2[currentmove][movecount],120,200),True,False),playerx,playery)
    else:
        displayimage(display,scaleimage(moves2[currentmove][movecount],120,200),playerx,playery)
    
    movecount+=1
    playerx+=playerxspeed
    playery+=playeryspeed
            

    return currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction