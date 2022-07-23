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

# loading the image of the rode
rode = pygame.image.load("sprites/ninja/rode.png")


def playing(display,player,currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist):

    # if currentmove == "attack":
    #     playmusic("audio/punch1.mp3")
    # all the events while playing the game over heres
    keys = pygame.key.get_pressed()
    
    for e in pygame.event.get():
        if keys[pygame.K_s]:
            currentmove = "slide"
            if direction == 0:
                playerxspeed=-20
            else:
                playerxspeed=20

        elif e.type==pygame.QUIT:
            sys.exit()
            
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                playerxspeed=10
                currentmove = "run"
                direction=1
            elif e.key == pygame.K_LEFT:
                playerxspeed=-10
                currentmove = "run"
                direction=0
            elif e.key == pygame.K_SPACE:
                print("pressed")
                if not jumped:
                    currentmove = "jump"
                    if direction==0:
                        playerxspeed=-30
                    else:
                        playerxspeed=30
                    playeryspeed=-30
                    jumped = True
                    
            elif e.key == pygame.K_f:
                print("hello world")
                currentmove = "attack"
                movecount = 0

            elif e.key == pygame.K_t:
                if not throwing:
                    currentmove="throwrode"
                    movecount = 0
                    throwing = True
                    throwx = playerx
                    throwy = playery
                    rodedirection = direction

        if e.type == pygame.KEYUP:
            if not jumped:
                playerxspeed=0
                playeryspeed=0
                currentmove = "idle"


    # checking whether moves left or not if not it is seted to 0 again
    if movecount==len(moves2[currentmove]):
        movecount=0
        if currentmove == "throwrode":
            if throwing:
                throwing = False
                currentmove = "idle"

        if currentmove == "slide":
            playerxspeed = 0

        if jumped:
            jumped = False
            currentmove = "idle"
            playery = height-360
            playeryspeed=0
            playerxspeed=0
            jumped = False

    if not pygame.mixer.music.get_busy():
        playmusic("audio/zombiegroup.mp3")

    display.fill("white")

    displayimage(display,background,0,0)

    # displaying the zombies over here code below👇
    


    # displaying the character over here

    if throwing:
        displayimage(display,pygame.transform.flip(rode,True if rodedirection==0 else False,False),throwx,throwy)
        # if throwx==playerx:
        throwx+=-20 if rodedirection==0 else 20
        if throwx>width or throwx<0:
            throwing=False
            throwx=playerx


    if direction==0:
        displayimage(display,pygame.transform.flip(scaleimage(moves2[currentmove][movecount],120,200),True,False),playerx,playery)
    else:
        displayimage(display,scaleimage(moves2[currentmove][movecount],120,200),playerx,playery)
    
    movecount+=1
    playerx+=playerxspeed
    playery+=playeryspeed
            

    return currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist