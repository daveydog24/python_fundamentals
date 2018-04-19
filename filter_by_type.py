first_list = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]

current_tester = first_list
current_type = type(current_tester) 
if current_type is int: #int test
	if current_tester >= 100:
		print "That’s a big number!"
	else:
		print "That’s a small number"
elif current_type is str: #string test
	if len(current_tester) >= 50:
		print "Long sentence"
	else:
		print "Short Sentence"
elif isinstance(current_tester, first_list): # list test
	if len(current_tester) >= 10:
  		print "Big list!"
	else:
		print "Short list."


