# creating the playing screen it will be further used in the main.py where the main game is running
from numpy import place
import pygame
import sys
from resources.functions import playmusic,displayimage,displaytext,listallthefiles,scaleimage,drawrect

pygame.init()

width = 1200
height = 700

background = pygame.transform.scale(pygame.image.load("sprites/back/background.jpg"),(width,height))

location1 = "sprites/ninja"


# all the move

moves = ["idle","attack","glide","jump","dead","run","throwrode","slide"]
moves2 = {}
# appending all the moves to the obj 
for i in range(len(moves)):
    moves2.__setitem__(moves[i],listallthefiles(f"{location1}/{moves[i]}"))


# laodin the zombies moves
zombiemoves = ["idle","attack","walk","dead"]
zombiemoves2 = {}

for i in range(len(zombiemoves)):
    obj = {
        "male":listallthefiles(f"sprites/zombie/male/{zombiemoves[i]}"),
        "female":listallthefiles(f"sprites/zombie/female/{zombiemoves[i]}")
    }
    zombiemoves2.__setitem__(zombiemoves[i],obj)

# loading the image of the rode
rode = pygame.image.load("sprites/ninja/rode.png")

pygame.time.set_timer(pygame.USEREVENT, 20000)

def playing(display,player,currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist,zombiescount,noofthrow,kills):

    if playerx<0 or playerx>width:
        health-=0.1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_q] and keys[pygame.K_u] and keys[pygame.K_i] and keys[pygame.K_t]:
        health=0
    
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            zombiescount += 1
            noofthrow+=1
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
                if not jumped:
                    currentmove = "jump"
                    if direction==0:
                        playerxspeed=-40
                    else:
                        playerxspeed=30
                    playeryspeed=-30
                    jumped = True
                    
            elif e.key == pygame.K_f:
                currentmove = "attack"
                movecount = 0

            elif e.key == pygame.K_t:
                if not throwing:
                    if noofthrow>0:
                        currentmove="throwrode"
                        movecount = 0
                        throwing = True
                        throwx = playerx
                        throwy = playery
                        rodedirection = direction
                        noofthrow-=1

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
    for i in range(len(zombieslist)):

        # getting all the values
        zombiex = zombieslist[i]["zombiex"]
        zombiey = zombieslist[i]["zombiey"]
        zombiecurrentmove = zombieslist[i]["currentmove"]
        zombiemovementcount = zombieslist[i]["movecount"]
        zombiedirection = zombieslist[i]["direction"]
        zombiehealth = zombieslist[i]["health"]
        zombiegender = zombieslist[i]["gender"]
        zombieattacking = zombieslist[i]["attacking"]
        zombiespeedx = zombieslist[i]["speedx"]
        zombiehealthbarcolor = zombieslist[i]["healthbarcolor"]

        # If distance between zombie and player is less than 10 than the player health is reduce
        if abs(zombiex-playerx)<10 and zombiecurrentmove=="attack":
            if health>0:
                health-=0.5

        if zombiex==playerx and zombiecurrentmove!="dead":
            if health>0:
                health-=0.5

        if zombiecurrentmove=="attack":
            if zombieslist[i]["movecount"]>4:
                health-=0.5

        zombiemovecount = len(zombiemoves2[zombiecurrentmove][zombiegender])
        movecountupdate = 0
        if abs(zombiex-playerx)<10:
            zombieslist[i].update({
                "currentmove":"attack",
                "movecount":0
            })

        if zombiecurrentmove=="attack" and zombiemovementcount==zombiemovecount-1:
            zombieslist[i].update({
                "currentmove":"walk",
                "attacking":False
                
            })

        # displaying the zombie according to their position left or right
        if zombiedirection==0:
            displayimage(display,scaleimage(pygame.transform.flip(zombiemoves2[zombiecurrentmove][zombiegender][zombiemovementcount],True,False),200,200),zombiex,height-350)
        else:
            displayimage(display,scaleimage(zombiemoves2[zombiecurrentmove][zombiegender][zombiemovementcount],200,200),zombiex,height-350)

        # displaying the zomibes health
        drawrect(display,zombiehealthbarcolor,zombiex+30,zombiey-10,zombiehealth,10)


        movecountupdate = 1 if zombiemovementcount<zombiemovecount-1 else 0
        
        # moving the zombie in the player direction and hitting the player
        zombieslist[i].update({
            "movecount":zombieslist[i]["movecount"]+movecountupdate if movecountupdate==1  else 0,
            "zombiex":zombiex + zombiespeedx if zombiex<playerx else zombiex-zombiespeedx if not zombieattacking else zombiex,
            "direction":0 if zombiex>playerx else 1
        })

        # checking whether the user has collided with the hammer or not
        if abs(throwx-zombiex)<10:
            if throwing:
                zombieslist[i].update({
                    "health":0
                })
                throwing = False

        
        # checking the zombies health and if less than or equal to 0 then the zombie is removed
        if zombiehealth<1:
            zombieslist.remove(zombieslist[i])
            kills+=1
            break

        if currentmove=="attack" and abs(playerx-zombiex)<40:
            zombieslist[i].update({
                "health":zombieslist[i]["health"]-5
            })


    # displaying the character over here

        # displaying the rode if thrown
    if throwing:
        displayimage(display,pygame.transform.flip(rode,True if rodedirection==0 else False,False),throwx,throwy+50)
        throwx+=-30 if rodedirection==0 else 30
        if throwx>width or throwx<0:
            throwing=False
            throwx=playerx

        
        # displaying the character according to the direction
    if direction==0:
        displayimage(display,pygame.transform.flip(scaleimage(moves2[currentmove][movecount],120,200),True,False),playerx,playery)
    else:
        displayimage(display,scaleimage(moves2[currentmove][movecount],120,200),playerx,playery)

    # incrementing the position of the user and the move
    movecount+=1
    playerx+=playerxspeed
    playery+=playeryspeed

    # displaying the health bar over here

    drawrect(display,"red",10,10,health*2,30)
    displaytext(display,f"{int(health)}",health+3,10,36,"blue",False,False)
    displaytext(display,f"Kills:-{kills}",500,10,50,"blue",True,True)
    displayimage(display,rode,width-250,20)
    displaytext(display,f"{noofthrow}",width-90,20,60,"black",False,False)


    return currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist,zombiescount,noofthrow,kills