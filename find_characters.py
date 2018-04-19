def find(word_list, char): #function takes in a list and then the character for the test
    new_list = [] #creates an empty list everytime we are testing within the function
    for count in range(0, len(word_list)): #goes through each index of the list
        if word_list[count].find(char) != -1: #test each word in the list for the character and if found starts the conditional
            new_list.append(word_list[count]) #adds the new word found with the character tested above
    print new_list #prints the new list once the loop has finished and all words were checked

test_list = ['hello','world','my','name','is','Anna','hello','world','my','name','is','Anna']
find(test_list, 'o')