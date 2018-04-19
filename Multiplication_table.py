
#answer key
print '  x  1  2  3  4  5  6  7  8   9  10  11  12'
for row in range(1, 12 + 1): 
    display_string  = ''
    for column in range(1, 13):
        if column == 1:
        	display_string += ' ' + str(row) + ' ' + str(column * row)
        elif column < 7 and (column * row) < 100:
            display_string += ' ' + str(column * row)
        elif column == 7 and (column * row) <= 72:
            display_string += '  ' + str(column * row)
        elif column == 7 and (column * row) >= 81 and (column * row) < 90:
            display_string += ' ' + str(column * row) + ' '
        elif column == 8 and (column * row) <= 90:
        	display_string += '  ' + str(column * row)
        elif column == 9 and (column * row) <= 90:
        	display_string += '  ' + str(column * row)
        elif column == 10 and (column * row) <= 99:
        	display_string += '  ' + str(column * row)
        else:
            display_string += ' ' + str(column * row)
        # display_string += ' ' + str(column * row)
    print display_string    
