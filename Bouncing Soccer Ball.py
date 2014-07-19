'''
Simple Bouncing Ball program, written in Python 2.7 using Pygame. Features:
	Damping effect on hitting walls.
	Speed of ball decreases gradually due to friction.
	Click to kick the ball.
	***********************
	Future Scope:
	Add more balls.
	Replace mouse cursor.
	*********************
	Author: Debojeet Chatterjee
'''

bif = "bg.jpg"
mif = "ball.png"

import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Click to Kick Soccer Ball")

background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()

x = 0
y = 0
clock = pygame.time.Clock()
speed_x = 200
speed_y = 300
#Gives direction of ball movement, reversed on each wall hit to give a bouncy effect
dir_x = 1
dir_y = 1

while True:
	ms = clock.tick()
	sec = ms/1000.0
	#Gradual decrease in speed due to friction
	speed_x*=0.9999
	speed_y*=0.9999
	#Calculate amount of movement to be done
	move_x = sec*speed_x
	move_y = sec*speed_y
	#Check for events
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==MOUSEBUTTONDOWN: #Kick the ball
			(mx,my) = pygame.mouse.get_pos()
			if mx<(x+ball.get_width()) and mx>x and my<(y+ball.get_height()) and my>y: #Check if cursor lies within the ball
			#Speed up values
				speed_x*=2.5
				speed_y*=2.5
	screen.blit(background,(0,0))
	screen.blit(ball,(x,y))
	x+=dir_x*move_x
	y+=dir_y*move_y
    #Damping on wall collision
	if x>(screen.get_width()-ball.get_width()):
		speed_x*=0.8
		#print "X: %f, Y: %f" % (move_x,move_y)
		dir_x = -1
	elif x<0:
		speed_x*=0.8
		#print "X: %f, Y: %f" % (move_x,move_y)
		dir_x = 1
	elif y>(screen.get_height()-ball.get_height()):
		speed_y*=0.8
		#print "X: %f, Y: %f" % (move_x,move_y)
		dir_y = -1
	elif y<0:
		speed_y*=0.8
		#print "X: %f, Y: %f" % (move_x,move_y)
		dir_y = 1

	pygame.display.update()
pygame.quit()
