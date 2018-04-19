def draw_stars(my_list):
	for count in range(0, len(my_list)):
		if isinstance (my_list[count], int):
			print my_list[count] * "*"
		elif isinstance (my_list[count], str):
			letter = my_list[count]
			letter = letter[0]
			letter = letter.lower()
			print letter * len(my_list[count])

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
