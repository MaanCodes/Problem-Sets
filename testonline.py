from visual import *
import random
from math import sqrt, atan2
            
def collisions(scene):
    #check for colision against other balls
    for a in range(0, len(scene.objects)):
        for b in range(a+1, len(scene.objects)):
            dx = scene.objects[a].pos.x - scene.objects[b].pos.x
            dy = scene.objects[a].pos.y - scene.objects[b].pos.y
            #quick and dirty check to find that objects that are not going to collide
            if dx > 1: continue
            if dy > 1: continue
            #full collision check 
            distance = (dx*dx)+(dy*dy) # dont need sqrt atm as distance to check is 1
            if(distance < 1):
                diff = scene.objects[a].pos-scene.objects[b].pos
                diff = diff/sqrt(diff.x**2 +diff.y**2)    
                a_comp= diff*(scene.objects[a].velocity.x * diff.x + scene.objects[a].velocity.y * diff.y)
                b_comp= diff*(scene.objects[b].velocity.x * diff.x + scene.objects[b].velocity.y * diff.y)
                scene.objects[a].velocity= scene.objects[a].velocity - a_comp + b_comp
                scene.objects[b].velocity= scene.objects[b].velocity - b_comp + a_comp                
                #place second ball so not touching first
                mid_point= (scene.objects[a].pos + scene.objects[b].pos)/2                                
                angle = math.atan2(dy, dx)
                scene.objects[a].pos= mid_point+diff/2*1.0005
                scene.objects[b].pos= mid_point-diff/2*1.0005


    #check for collision against area bounds            
    for check in scene.objects:
        if(check.pos.x < -12):
            check.velocity = vector(abs(check.velocity.x), check.velocity.y, 0)            
        elif(check.pos.x > 12):
            check.velocity = vector(-abs(check.velocity.x), check.velocity.y, 0)            
        elif(check.pos.y < -12):
            check.velocity = vector(check.velocity.x, abs(check.velocity.y), 0)
        elif(check.pos.y > 12):
            check.velocity = vector(check.velocity.x, -abs(check.velocity.y), 0)

random.seed()
scene = display(title='Bouncy Balls', width=500, height=500, center=(0,0,0), background=(0,0,0))
scene.autoscale = 0
delta=0.1
scene.range = (-25, -25, -25)

for i in range(0, 30):
    ball = sphere(pos=(random.randint(-10, 10), random.randint(-10, 10), 0),color=(1, 1, 1),radius=0.5)
    ball.speed = float(random.randint(1, 5))/2
    ball.velocity = vector(cos(radians(i*60)), sin(radians(i*60)), 0)

while 1:
    rate(60)
    for ball in scene.objects:
        ball.pos = ball.pos + (ball.velocity*delta*ball.speed)
    collisions(scene)
Last edited by mike_g; February 4th, 2009 at 05:15 PM.
Advanced reply Adv Reply  
February 4th, 2009 #6 crazyfuturamanoob's Avatar crazyfuturamanoob  crazyfuturamanoob is offline
May the Ubuntu Be With You!

Join Date
Jan 2008
Location
Whenever the food is.
Beans
1,203
Distro
Kubuntu
Re: Cool Python Scripts/Small Programs
Here you go:
Code:
import os

while 1:
    os.system( "eject /dev/scd0" )
It makes sure you can't close your CD/DVD drive tray.

There's no way to stop it but kill python interpreter process.
Keyboard not found!

Press any key to continue...
Advanced reply Adv Reply  
February 4th, 2009 #7 Xcmd's Avatar Xcmd  Xcmd is offline
First Cup of Ubuntu

Join Date
Jan 2009
Beans
11
Re: Cool Python Scripts/Small Programs
A simple program I wrote for catching a bouncing ball. This utilizes Pygame... because I was bored and was trying to teach myself blitting and such. I'm sure it could be done a lot better.

Code:
#Catch the Ball by Xcmd
#
#A very simple game: just move the mouse and try to get the pointer over the ball.

#Import the good stuff! Read tutorials to find out why...
import sys, pygame, random
from pygame.locals import *

#Check if the fonts module loaded. If not, oosp.
if not pygame.font: print "Fonts disabled!"
pygame.init()
random.seed(pygame.time.get_ticks())

#Random numbers for some reason... hmm... what could r g b mean?
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

#Defining some stuff... size... speed... black?!
size = width, height = 800, 600
speed = [1, 1]
black = 0,0,0

#Setting up the screen the player sees. See how size comes from
#up there to down here? Nifty!
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Catch the Ball!")

#Yes, I literally made a .png of a ball...
#I'm using convert_alpha() because I want to use the PNG's
#transparency layer instead of defining one myself. This
#also helps speed things up as far as the game goes because
#the game doesn't have to keep converting the PNG file into
#a useable graphic format. .convert() does the same thing
#but does not include transparency.
ball = pygame.image.load('ball.png').convert_alpha()

#Rects are your friends. Please read up on them.
ballrect = ball.get_rect()

#Hey, I remember r g b!
fontColor = r,g,b

#Oh honh honh! Zee font! She is Tres Arial!
font = pygame.font.SysFont("Arial Black", 25)

#winText is a surface... just in case you didn't know..
winText = font.render('You caught the ball! [Click to Play Again]', 0, fontColor)

#Look, another rect!
winRect = [0,0,0,0]

#Are we currently in a state where we've caught the ball?
caught = 0

#This is just because I wanted to show an updating surface that's
#a little more obvious than the ball zipping around.

#tix = ticks. How many ticks have passed since this was called?
tix = pygame.time.get_ticks()

#tixText = a surface!
tixText = font.render(str(tix), 0, fontColor)

#Hmm... another rect... why did I define it as nothing?
tixRect = [0,0,0,0]

#How many times did we catch the ball? Tell the user!
caughtAmt = 0
caughtText = font.render("Caught: " + str(caughtAmt), 0, fontColor)
caughtRect = [0,0,0,0]

#MAIN LOOP GO GO GO!
while 1:
	
	#Update the Tix! WOO!
	tix = pygame.time.get_ticks()
	tixText = font.render(str(tix), 0, fontColor)
	
	#Check some events. WICKED.
	for event in pygame.event.get():
		#QUITTERS QUIT, MEG!
		if event.type == pygame.QUIT:
			print "Quit event detected. Good bye!"
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			#DING FRIES ARE DONE.
			ding = event.pos
			
			#Did the mouse collide with the rect of the ball? THEN WE CAUGHT IT! YEY!
			if ballrect.collidepoint(ding) and caught != 1:
				caught = 1
				caughtAmt = caughtAmt + 1
				caughtText = font.render("Caught: " + str(caughtAmt), 0, fontColor)
		
		#Okay, so this only works when we caught the ball. If we click
		#the mouse, then we get to go again.
		if event.type == pygame.MOUSEBUTTONUP:
			if caught == 1 and event.button == 1:
				caught = 0
				speed[0] = speed[0] + 1
				speed[1] = speed[1] + 1
	
	#LIGHTNING SPEED GO! If the left-side of the ballrect is at or less
	#than the 0 position of the left-hand side of the screen OR it is
	#GREATER than or EQUAL TO the RIGHT HAND side of the screen...
	#then we need to change the direction. Same thing for top and bottom.
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
	
	#fill the back of the screen with black
	screen.fill(black)
	
	#draw us a ball!
	screen.blit(ball, ballrect)
	
	#draw the surface caughtText in the upper-right
	caughtRect = screen.blit(caughtText, (600, 0))
	
	#draw the surface of the ticks counter in the upper-left
	tixRect = screen.blit(tixText, (0,0))
	
	#IF and ONLY IF we're currently in the "caught ball" state...
	#draw the winText. Oh, also prevent the ball from moving.
	if caught == 1:
		winRect = screen.blit(winText, (50, 350))
		speed = [0, 0]
	
	#What are we updating? Everything!
	updates = ballrect, tixRect, winRect, caughtRect
	pygame.display.update(updates)
(And, yes, I did attach the ball.png ... it's just a white ball...)
Attached Images Attached Images
File Type: png ball.png (459 Bytes, 395 views)
AMD Phenom X64 Quadcore 1.8 GHz / 4 GB RAM / 500 GB HDD / GeForce 8400 GS / Lively 32-Bit / Vista 64-Bit
Advanced reply Adv Reply  
February 5th, 2009 #8 bgs100's Avatar bgs100  bgs100 is offline
A Carafe of Ubuntu

Join Date
Oct 2008
Location
$HOME
Beans
112
Distro
Ubuntu 11.10 Oneiric Ocelot
Re: Cool Python Scripts/Small Programs
Edit: NEVERMIND. JUST IGNORE THIS. USE IT ONLY FOR FINDING OUT WHAT THE FUTURE POSTS ARE TALKING ABOUT WHEN THEY REFER TO THIS.



This nice program has been made to do your math homework:
PHP Code:
#!/usr/bin/python

import os
a=0
pi = 3.14
b=0
c=""
x=int(raw_input("Enter number of problems: "))        
while a != x:
    a = a+1
    b=raw_input("%i. " % (a))
    b=os.popen("awk 'BEGIN {print %s}'" % (b)).read()
    b=b[:-1]
    c = ("%s. %s\n" % (a, b)) + c
print "\n%s\n" % ('\n'.join( reversed(c.split('\n')) ))  
Last edited by bgs100; June 2nd, 2009 at 02:12 PM.
$(fortune)
In a world without walls and fences, who needs windows and gates?
Advanced reply Adv Reply  
February 5th, 2009 #9 snova's Avatar snova  snova is offline
Ubuntu Cappuccino Scuro

Join Date
May 2008
Beans
Hidden!
Re: Cool Python Scripts/Small Programs
Quote Originally Posted by bgs100  View Post
PHP Code:
    b=os.popen("awk 'BEGIN {print %s}'" % (b)).read() 
    b=b[:-1]  
How about using built in tools? 

PHP Code:
      b = eval(b)  
 Advanced reply Adv Reply  
February 5th, 2009 #10 ghostdog74  ghostdog74 is offline
I Ubuntu, Therefore, I Am

Join Date
Sep 2006
Beans
2,914
Re: Cool Python Scripts/Small Programs
Quote Originally Posted by bgs100  View Post
This nice program has been made to do your math homework:
PHP Code:
#!/usr/bin/python 

import os 
a=0 
pi = 3.14 
b=0 
c="" 
x=int(raw_input("Enter number of problems: "))         
while a != x: 
    a = a+1 
    b=raw_input("%i. " % (a)) 
    b=os.popen("awk 'BEGIN {print %s}'" % (b)).read() 
    b=b[:-1] 
    c = ("%s. %s\n" % (a, b)) + c 
print "\n%s\n" % ('\n'.join( reversed(c.split('\n')) ))  
that's not really "cool" is it? mixing different programming tools like that. If you want to use Python, do everything in Python.
Python tutorial |Unix power tools|Effective AWK|A handful of Awk|Perl|File Renamer|Bash ref
Advanced reply Adv Reply  
