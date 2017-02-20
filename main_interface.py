	
		lev1 = [
       "",
       "",
       "",
       "",
       "",
       "              ",
       "  ---           ----  ",
       "   -----          ---- ",
       "      ----       ----  ",
       "--------------------------"]
	
	
	def render_stage2 (self):

		adventure_screen.blit(background, (0, 0))

		self.block_group.draw (adventure_screen)
		start_screen.blit(font1.render (str(self.a), True, (250,250,250)),(0,0))


	def stage2_loop (self):

		self.a = timer.get_fps()

		if self.constructor2 == False:
			self.create_level (lev2)
			self.constructor2 = True

		self.render_stage2 ()
		timer.tick (30)
		pygame.display.flip() 