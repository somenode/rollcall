import csv
from itertools import chain

numstudents = input('Enter the number of students [e.g.- 25]:\t')
points = input('Enter the number of points per absence [e.g.- 3]:\t')

studentlist = ["Student"]
totalpoints = ["Points removed"]

def class_size(numstudents):
	x = numstudents
	return x

def student_name(student):
	y = student
	return y

def points_removed(points):
	z = (points*absences)
	return z

count = 0
while count < numstudents:
	
	i = -1
	j = -1
	if i < len(studentlist) and j < len(totalpoints):

		#take input
		student = raw_input('Enter student\'s name:\t')
		#append to list
		studentlist.append(student)
		#note position
		student = studentlist[i]

		absences = input('Enter how many times student was absent:\t')
		totalpoints.append(points_removed(points))
		z = totalpoints[j]
		#print statement
		print "Student name: ", student, "\tPoints off: ", z
		i = i + 1
		j = j + 1

	else:
		break

	count += 1

print "All Done! Open your rollcall.csv file to see the results!"
#csv output 
#path can be changed
w = csv.writer(file('rollcall.csv', 'wb'), dialect = 'excel')
sheet = studentlist, totalpoints
w.writerows(sheet)



