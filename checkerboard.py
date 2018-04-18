def checkerboard(lines, stars): # easily changable function to customize how many stars there are in each line and how many lines 
	switch = 1 #decides which type of stars to print and alternates
	for count in range (0, lines):
		if switch == 1:
			print ("* " * stars)
			switch = 2
		elif switch == 2:
			print (" *" * stars)
			switch = 1

checkerboard(20, 80)
