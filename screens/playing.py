# creating the playing screen it will be further used in the main.py where the main game is running
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
    # print("the lj")
    obj = {
        "male":listallthefiles(f"sprites/zombie/male/{zombiemoves[i]}"),
        "female":listallthefiles(f"sprites/zombie/female/{zombiemoves[i]}")
    }
    # print(obj)
    zombiemoves2.__setitem__(zombiemoves[i],obj)
    # print(zombiemoves2)

# print(zombiemoves2)

# loading the image of the rode
rode = pygame.image.load("sprites/ninja/rode.png")

pygame.time.set_timer(pygame.USEREVENT, 20000)

def playing(display,player,currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist,zombiescount,noofthrow,timing,kills):

    if playerx<0 or playerx>width:
        health-=0.1

    keys = pygame.key.get_pressed()
    
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT: 
            zombiescount += 1
            noofthrow+=1
            print("enhanced")
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
                        playerxspeed=-40
                    else:
                        playerxspeed=30
                    playeryspeed=-30
                    jumped = True
                    
            elif e.key == pygame.K_f:
                # print("hello world")
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

        # If distance between zombie and player is less than 10 than the player health is reduce
        if abs(zombieslist[i]["zombiex"]-playerx)<10 and zombieslist[i]["currentmove"]=="attack":
            if health>0:
                health-=0.5

        if zombieslist[i]["zombiex"]==playerx and zombieslist[i]["currentmove"]!="dead":
            if health>0:
                health-=0.5

        if zombieslist[i]["currentmove"]=="attack":
            if zombieslist[i]["movecount"]>4:
                print("hitted")
                health-=0.5

        zombiemovecount = len(zombiemoves2[zombieslist[i]["currentmove"]][zombieslist[i]["gender"]])
        movecountupdate = 0
        if abs(zombieslist[i]["zombiex"]-playerx)<10:
            # print("updated")
            zombieslist[i].update({
                "currentmove":"attack",
                "movecount":0
            })

        if zombieslist[i]["currentmove"]=="attack" and zombieslist[i]["movecount"]==zombiemovecount-1:
            print("entered")
            zombieslist[i].update({
                "currentmove":"walk",
                "attacking":False
                
            })

        # displaying the zombie according to their position left or right
        if zombieslist[i]["direction"]==0:
            displayimage(display,scaleimage(pygame.transform.flip(zombiemoves2[zombieslist[i]["currentmove"]][zombieslist[i]["gender"]][zombieslist[i]["movecount"]],True,False),200,200),zombieslist[i]["zombiex"],height-350)
        else:
            displayimage(display,scaleimage(zombiemoves2[zombieslist[i]["currentmove"]][zombieslist[i]["gender"]][zombieslist[i]["movecount"]],200,200),zombieslist[i]["zombiex"],height-350)

        # displaying the zomibes health
        drawrect(display,zombieslist[i]["healthbarcolor"],zombieslist[i]["zombiex"]+30,zombieslist[i]["zombiey"]-10,zombieslist[i]["health"],10)


        movecountupdate = 1 if zombieslist[i]["movecount"]<zombiemovecount-1 else 0
        
        # moving the zombie in the player direction and hitting the player
        zombieslist[i].update({
            "movecount":zombieslist[i]["movecount"]+movecountupdate if movecountupdate==1  else 0,
            "zombiex":zombieslist[i]["zombiex"] + zombieslist[i]["speedx"] if zombieslist[i]["zombiex"]<playerx else zombieslist[i]["zombiex"]-zombieslist[i]["speedx"] if not zombieslist[i]["attacking"] else zombieslist[i]["zombiex"],
            "direction":0 if zombieslist[i]["zombiex"]>playerx else 1
        })

        # checking whether the user has collided with the hammer or not
        if abs(throwx-zombieslist[i]["zombiex"])<10:
            if throwing:
                zombieslist[i].update({
                    "health":0
                })
                throwing = False

        
        # checking the zombies health and if less than or equal to 0 then the zombie is removed
        if zombieslist[i]["health"]<1:
            zombieslist.remove(zombieslist[i])
            kills+=1
            break

        if currentmove=="attack" and abs(playerx-zombieslist[i]["zombiex"])<40:
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
    displaytext(display,f"Timing:-{str(timing)}",400,10,50,"black",True,True)
    displaytext(display,f"Kills:-{kills}",700,10,50,"blue",True,True)


    return currentmove,playerx,playery,playerxspeed,playeryspeed,movecount,direction,jumped,throwing,throwx,throwy,rodedirection,health,zombieslist,zombiescount,noofthrow,kills