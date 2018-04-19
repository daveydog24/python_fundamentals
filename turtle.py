# try this either as a .py file or in the python shell
import turtle
# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.backwards(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20


# keep getting this error and so i dont know how to work on this project....... 

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "turtle.py", line 10, in <module>
#     turtle.right(90)
# AttributeError: 'module' object has no attribute 'right'
# >>> 




^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^