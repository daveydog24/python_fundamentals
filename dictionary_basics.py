def dictionary_basics(my_list):
	for key, data in my_list.items():
		if key == 'name':
			print "My name is", data
	for key, data in my_list.items():
		if key == 'age':
			print "My age is", data
	for key, data in my_list.items():
		if key == 'country':
			print "My country of birth is", data
	for key, data in my_list.items():
		if key == 'favorite':
			print "My favorite language is", data
			print ""

david = {}
david['name'] = "David Wukelic"
david['age'] = "30"
david['country'] = "The United States"
david['favorite'] = "Python"

kim = {"name": "Kimberly Lyle", "age": "26", "country": "The United States", "favorite": "Java"}

dictionary_basics(david)
dictionary_basics(kim)