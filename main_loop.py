done = True

def main ():
	while done:

		for e in pygame.event.get ():
				if e.type == pygame.QUIT:
					sys.exit ()
				if e.type == event1+1:
					c = x

		

		


		xx += 1
		x += timer.tick (30)
		window.blit(start_screen, (10, 10))
		start_screen.fill ((123,12,45))
		start_screen.blit (rect1, ((x/30),100))
		b = pygame.time.get_ticks ()
		rect1.fill ((xx,xx,xx))

		
		
		a = timer.get_fps()
		start_screen.blit(font1.render (str(a), True, (250,250,250)),(0,0))

		start_screen.blit(font1.render (str(b), True, (250,250,250)),(15,15))
		start_screen.blit(font1.render (str(x), True, (250,250,250)),(30,30))
		start_screen.blit(font1.render (str(c), True, (250,250,250)),(100,30))
		#pygame.time.delay(60)

		pygame.display.flip() 