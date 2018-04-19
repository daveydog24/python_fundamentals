def foo_bar(num):
	foo_button = True
	bar_button = False
	for x in range(100, num):
		for count in range(2, x):    
			if x % count == 0:
				foo_button = False
			if x**(1.0/2) == count:
				bar_button = True
		if foo_button == True:
			print x, "Foo"
		elif bar_button == True:
			print x, "Bar"
		elif foo_button == False and bar_button == False:
			print x, "Foobar"
		foo_button = True
		bar_button = False


foo_bar(10000)