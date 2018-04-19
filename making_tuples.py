my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def making_tuples(my_dict): #function that takes in an argument in the 
							#paramter my_dict and will print an update list of tuples

    new_list = [] #creates and empty list each time the function is called

    for keys, value in my_dict.iteritems(): #looks for the keys (:) and values that follow throughout 
    										#the whole dictionary

        new_list.append((keys, value))# adds the key and attached value as a tuple to the new list 
        							  # and this is in a loop till it has gone through each part 
        							  # of the dictionary
    return new_list #returns the list

new_list = making_tuples(my_dict) #stores new_list with the value of whatever dictionary you pass into the function
print new_list #prints the new_list