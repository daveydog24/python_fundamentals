def odd_even(num):
	for count in range (1, num + 1):
		if count % 2 == 0:
			print "Number is " + str(count) + ". This is an even number."
		else:
			print "Number is " + str(count) + ". This is an odd number."
			
odd_even(2000)

def multiply(my_list, second_argument):
	for count in range(0, len(my_list)):
		my_list[count] = my_list[count] * second_argument
	return my_list

a = [2,4,10,16]
x = multiply(a, 10)
print x

def layered_multiples(arr):
	new_array = []
	for count in arr:
		second_arr = []
		for second_count in range(0, count):
			second_arr.append(1)
		new_array.append(second_arr)
	return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
