'''
experiment with operators (arithmetic, comparison, and logical operators): math class

Author: Landon Harrison
Version: 01/08/2025
'''
print("\n")
print("hi class! Today we are reviewing operators such as arithmetic, comparison, and truth statements\n")

#truth value gets reassigned each time a student answers a question

print("Teacher: Does anyone know what 5 plus 2 is?")
print("Student: Is it 7?")
addition = 5 + 2
truthVal = (addition == 7) #checking if student got the addition right 
print("Teacher: that is", truthVal)

print("\n")

print("Teacher: Does anyone know what 6 minus 4 is?")
print("Student: Is it 3?")
subtraction = 6 - 4
truthVal = (subtraction == 3) #checking if student got the subtraction right 
print("Teacher: that is", truthVal, ". It is 2.")

print("\n")

print("Teacher: Does anyone know what 5 multiplied by 4 is?")
print("Student: Is it 20?")
multiplication = 5 * 4
truthVal = (multiplication == 20) #checking if student got the multiplication right 
print("Teacher: that is", truthVal)

print("\n")

print("Teacher: Does anyone know what 20 divided by 4 is?")
print("Student: Is it 6?")
division = 20 / 4
truthVal = (division == 6) #checking if student got the multiplication right 
print("Teacher: that is", truthVal, "It is 5.")

print("\n")

print("Teacher: Is it true that 6 multiplied by 3 is larger than 5 multiplied by 4?")
comparison = (6 * 3) > (5 * 4) #calculating students answer 
print("Student: I think it is" , comparison)
print("Teacher: good job, you are right.")

print("\n")