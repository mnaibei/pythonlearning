print('Welcome to grade calculator')
grade = int(input('Please enter the Grade '))
#print('enter blank line to designate the end')

if grade>=80 and grade<=100:
	print('A')


elif grade>=70 and grade<=80:
    print("Your Grade is B")

elif grade>=50 and grade<=60:
    print("Your Grade is C")

elif grade>=33 and grade<=40:
    print("Your Grade is D")
    
elif grade>=20 and grade<=30:
    print("Your Grade is E")


else:
	print('Not Valid')

#grades={'A = 80', 'B =60', 'C =40'}
#num_courses = 0
#total_points = 0
#done = False

#while not done:
#    grade = input()
#if grade == '':
    #done = True

#elif grade not in points:
   # print("unknown grade '{0}' being ignored".format(grade))
#else:
   # num_courses += 1
    #total_points += points[grade]

#if num_courses > 0:
    #print('your grade is {grade}')
    