words = "It's thanksgiving day. It's my birthday,too!"
words.find("day") 
words2 = words
words2.replace("day", "month")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x.sort()
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]

newx = [x[0], x[len(x) - 1]]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
first_list = x[:len(x)/2] 
second_list = x[len(x)/2:] 
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list
