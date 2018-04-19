import random

def grade_generator(students):
	letter_grade =''
	print "Scores and Grades"
	for i in range(1, students):
		grade = random.randint(60,100)
		if grade >= 60 and grade <= 69:
			letter_grade = 'D'
			print "Score:", grade, "; Your grade is ", letter_grade
		elif grade >= 70 and grade <= 79:
			letter_grade = 'C'
			print "Score:", grade, "; Your grade is ", letter_grade
		elif grade >= 80 and grade <= 89:
			letter_grade = 'B'
			print "Score:", grade, "; Your grade is ", letter_grade
		else:
			letter_grade = 'A'
			print "Score:", grade, "; Your grade is ", letter_grade

grade_generator(10)