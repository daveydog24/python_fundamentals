#Muliples
#Part 1  This will print numbers 1-1000
for count in range(1,1001):
	if count % 2 == 1:
		print count

# Part 2 This will print all the multiples of 5 once the if statement makes sure its divisible by 5
for count in range(5,10000001):
	if count % 5 == 0:
		print count

#SUM, This will print the sum of all the values in a list
Counter = 0
for count in range(0, len(list)):
	Counter += list[count]
	print Counter

# AVERAGE LIST, This will print the average of the values in a list.
Counter = 0
for count in range(0, len(list)):
	Counter += list[count]
	Counter = Counter / len(list)
print Counter