def test_type(new_list):
	int_sum = 0
	string_sum = ''

	for value in new_list:
		if isinstance(value, int) or isinstance(value, float):
			int_sum += value
		elif isinstance (value, str):
			string_sum += value

	if int_sum > 0 and len(string_sum) > 0:
		print "This list you entered is of mixed type"
		print "String: " + string_sum
		print "Sum = ", int_sum
	elif int_sum > 0:
		print "This list you entered is of integer type"
		print "Sum = ", int_sum
	else: 
		print "This list you entered is of string type"
		print "String: " + string_sum