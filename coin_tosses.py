import random

def coinToss(num):
	print "Starting the program"
	head_count = 0
	tails_count = 0
	coin = 0
	for count in range(0, num + 1):
		coin = random.randint(0,1)
		coin = round(coin)
		if coin == 0:
			head_count += 1
			print "Attempt #" + str(count) + ": Throwing a coin... It's a head! ... Got", str(head_count),  "head(s) so far and", str(tails_count), "tail(s) so far"
		else:
			tails_count +=1
			print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! ... Got", str(head_count),  "head(s) so far and", str(tails_count), "tail(s) so far"
	print "Ending the program, thank you!"

coinToss(5000)