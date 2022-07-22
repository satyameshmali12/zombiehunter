# creating the home screen it will be further used in the main.py where the main game is running
import sys
import pygame

# bringing all the function from the resources folder
from resources.functions import loadimage,displayimage,displaytext,scaleimage,listallthefiles,playmusic

# width and height of the screen

width = 1200
height = 700

background = scaleimage(loadimage("sprites/back/ground.jpg"),1200,700)

# loading all the images of the male and female zombie :-state idle
zombiefrun = listallthefiles("sprites/zombie/female/walk")
zombiemrun  = listallthefiles("sprites/zombie/male/walk")


# loading the images
playbutton = pygame.transform.scale(pygame.image.load("sprites/gui/Play (4).png"),(130,130))
buttonx = 550
buttony = 240

# all the home code here👇

def home(display,zombiecount,zombie1x,zombie2x,zombie1xspeed,zombie2xspeed,place):
    
    # playing the music with the help of the playmusic function
    if not pygame.mixer.music.get_busy():
        playmusic("audio/homesound.mp3")

    # getting the events over here
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0]>buttonx and pos[0]<buttonx+playbutton.get_width() and pos[1]>buttony and pos[1]<buttony +playbutton.get_height():
                print("hello sir ")
                pygame.mixer.music.stop()
                place = "start_game"


    # displaying the backgoround of the home screen
    displayimage(display,background,0,0)

    
    # displaying all the button and text on the screen and their logic below
    displaytext(display,"Zombie Hunt",250,100,140,"white",True,True)

    displayimage(display,playbutton,buttonx,buttony)


    pygame.display.set_caption("Home")


    
    
    if zombiecount == len(zombiefrun):
        zombiecount=0

    # if zombie1
    # if speed = 3
    if zombie1xspeed>0:
        displayimage(display,scaleimage(zombiefrun[zombiecount],229,250),zombie1x,height-300)
    else:
        displayimage(display,pygame.transform.flip(scaleimage(zombiefrun[zombiecount],229,250),True,False),zombie1x,height-300)

    # flipping->transforming->displaying the image
    if zombie2xspeed<0:
        displayimage(display,pygame.transform.flip(scaleimage(zombiemrun[zombiecount],229,250),True,False),zombie2x,height-300)
    else:
        displayimage(display,scaleimage(zombiemrun[zombiecount],229,250),zombie2x,height-300)
    
    return zombiecount+1,zombie1x+zombie1xspeed,zombie2x+zombie2xspeed,place
    