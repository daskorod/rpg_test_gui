import classes
from pygame import sprite
import fonts
from screens import *
from constants import *
import text

def event_go ():
	c = 0

class Battle ():
	def __init__ (self):
		pass
	def turn (self, hero, monster):
		pass

def create_level (level):
	sprite_group = sprite.Group ()
	platforms = []
	#chests = []
	x = 0
	y = 0
	for row in level:
		for col in row:
			if col == "-":
				pf = classes.Platform (x,y)
				platforms.append (pf)
				sprite_group.add (pf)
			if col == "c":
				ch = classes.Chest (x,y)
				#chests.append (ch)
				sprite_group.add (ch)
			if col == "m":
				mn = classes.Monster (x,y,text.zombitext)
				sprite_group.add (mn)
			x += 45
		x = 0
		y += 45
	x = 0
	y = 0
	return  platforms, sprite_group


def render_text (text, control, a, s1):
	a_max = len(text)//350

	n = a*350

	if control.k_n == True:
		control.k_n = False
		s1 = text[n+0:n+50]
		if a < a_max+1:
			a = a+1
#		else:
#			a = 0

	#s1 = text[n+0:n+50]
	s1 = a
	s2 = a_max
	#s2 = text[n+50:n+100]
	s3 = text[n+100:n+150]
	s4 = text[n+150:n+200]
	s5 = text[n+200:n+250]
	s6 = text[n+250:n+300]
	s7 = text[n+300:n+350]
#	text = s1, s2, s3
	information_screen.blit(fonts.font2.render (str(s1), True, (250,250,250)),(2,0))
	information_screen.blit(fonts.font2.render (str(s2), True, (250,250,250)),(2,22))
	information_screen.blit(fonts.font2.render (str(s3), True, (250,250,250)),(2,44))
	information_screen.blit(fonts.font2.render (str(s4), True, (250,250,250)),(2,66))
	information_screen.blit(fonts.font2.render (str(s5), True, (250,250,250)),(2,88))
	information_screen.blit(fonts.font2.render (str(s6), True, (250,250,250)),(2,110))
	information_screen.blit(fonts.font2.render (str(s7), True, (250,250,250)),(2,132))


def text_split (text):
	s1 = text[0:50]
	s2 = text[50:100]
	s3 = text[100:150]
	return s1, s2, s3

