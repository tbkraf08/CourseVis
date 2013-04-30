#!/usr/bin/env python

f = open('bioCourses.txt', 'rb')

courses = []
course = ''
for line in f:
	if line.strip() == '':
		courses.append(course)
		course = ''
		continue

	course += line + '\n'

jsonCourses = []

for c in courses:
	count = 0 
	csplit = c.split('\n')
	jsonC = {}

	for cs in csplit:
		if cs.strip() == '':
			continue

		count += 1
		#print count
		#print cs
		#print 
		# course name
		if  count  == 1:
			jsonC['name'] = cs.strip()
			#print jsonC['name']

		# professor and when course is offered
		elif count == 2:
			if ')' in c:
				cs = cs.split(')')

				jsonC['professor'] = cs[0].replace('(','').strip()
				try:
					jsonC['offered'] = cs[1].strip().split(',')
				except:
					pass
			else:
				jsonC['offered'] = cs.strip().split(',')

		# preq's and description
		elif count == 3:
			jsonC['description'] = cs.strip()

		# credits
		elif count == 4:
			cs = cs.split()
			try:
				jsonC['credits'] = cs[1]
			except:
				pass	

	print jsonC
	print
	jsonCourses.append(jsonC)

