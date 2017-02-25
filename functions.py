import classes
from pygame import sprite


def event_go ():
	c = 0


def create_level (level):
	sprite_group = sprite.Group ()
	platforms = []
	chests = []
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
				chests.append (ch)
				sprite_group.add (ch)
			x += 45
		x = 0
		y += 45
	x = 0
	y = 0
	return  platforms, sprite_group, chests
