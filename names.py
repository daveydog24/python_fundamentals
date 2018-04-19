def names(my_list):
    first_name = ""
    last_name = ""
    for i in range(0, len(my_list)):
        for key, data in my_list[i].items():
            if key == "first_name":
                first_name = data;
            elif key == "last_name":
                last_name = data;
        print first_name, last_name

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

names(students)


def names(my_list): 
    first_name = "" #empty string primed to store first names
    last_name = "" #empty string primes to store last names
    length = 0 #created to store the amount of characters in names later
    count = 0 #created to count the amount of names in all the lists combined
    for title in my_list: #loop that goes through a dictionary and stores a title for each list within the dictionary
        print title #prints the title of list
        for person in my_list[title]: #enters a loop within the current list nested within the whole dictionary and stores the current list within
            count += 1 #starts and then adds to the count to see what line we are currently on
            for key, data in person.items(): #looks within the lists and stores a key and data for each item in the lists
                if key == "first_name": # if the key matches the title for first_name it will stores the data for that key
                    first_name = data.upper() #stores the variable first_name of the true statment and uppercases it
                elif key == "last_name": # if the key matches the title for last_name it will stores the data for that key
                    last_name = data.upper() #stores the variable last_name of the true statment and uppercases it
            length = len(first_name) + len(last_name) #changes length for the amount of characters total of the first and last name
            print count, "-", first_name, last_name, "-", length #prints the current count, - first and last name - and the total length of characters already stored

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


names(users)

