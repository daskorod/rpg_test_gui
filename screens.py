from pygame import Surface
from pygame import image
from pygame import display

window = display.set_mode((820, 620))
display.set_caption('Svinotest')

start_screen = Surface((800, 600))
background = image.load ('images/back.png')
adventure_screen = Surface ((800, 450))
instrumental_screen = Surface ((800,150))
hero_screen = Surface ((150,150))
monster_screen = Surface ((150,150))
information_screen = Surface ((500,150))