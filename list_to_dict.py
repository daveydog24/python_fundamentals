name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def making_dictionaires(list1, list2):
	temp_dict = zip(list1, list2)
	the_dict = dict(temp_dict)
    	return the_dict

the_dict = making_dictionaires(name, favorite_animal)
print the_dict