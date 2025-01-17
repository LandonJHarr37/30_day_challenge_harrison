'''
Using functions within a class as a simple calculator and for string reversal
    Then testing these functions with test cases

A function can be defined within a class to create a reusable portion of code 

Author: Landon Harrison
Version: 01/17/2025
'''

''' simple calculator
this function takes two numbers and an operator to conduct a math operation 
    possible operators *, +, -, /, %
    Will only take non decimal numbers (otherwise will truncate the decimal and notify user)
    Subtracts first second number from first, divides the first by the second, taking num1's mod of num2
'''
def simp_calc(num1, num2, operator):
    
    num = 0

    #truncates the decimal off of both numbers if present, and notifies user 
    if(num1 % 1 != 0):
        print(f"truncating the {(num1 % 1)} off of {num1} \n")
        num1 - (num1 % 1)
    if(num2 % 1 != 0):
        print(f"truncating the {(num2 % 1)} off of {num2} \n")
        num2 - (num2 % 1) 

    if(operator == "*"):
        num = num1 * num2
    elif(operator == "+"):
        num = num1 + num2
    
    #subtracts second number from the first
    elif(operator == "-"):
        num = num1 - num2
    #divides the first number by the second, also checks for an undefined division
    elif(operator == "/"):
        if(num2 == 0):
            print("undefined division\n")
            return
        num = num1/num2
    elif(operator == "%"):
        num = num1 % num2
    else:
        print("did not insert a valid operator.")
    
    print(f"The number for {num1}{operator}{num2} is: {num} \n")
    return


'''reversing string 
returns the reverse of a string using substring 
'''
def reversing_string(string):
    print(f"{string[::-1]}\n")


'''test cases'''

simp_calc(2, 3, "*") # should be 6

simp_calc(4, 3, "-")# should be 1

simp_calc(8, 2, "/")# should be 4

simp_calc(9, 3, "+")# should be 12 

simp_calc(12, 5, "%")# should be 2

simp_calc(6, 0, "/")# should be given an unefined message 

reversing_string("Hi my name is landon!")

#getting test cases from user

func_choice = input("Hi welcome to function plaza, please pick between doing a \nrssimple calculation or reversing a string ("\
      "respond with either sc or rs:")

if (func_choice == "sc"):
    num1 = int( input("Input an integer number (num1): "))
    num2 = int( input("Input an integer number (num2): "))
    operator = input("Input the operator you would like to use (*, -, +, /, %): ")
    simp_calc(num1, num2, operator)
elif (func_choice == "rs"):
    reversed_string = input("Please type a string to be reversed, make it silly: ")
    reversing_string(reversed_string)
else:
    print(f"input a valid choice of function, you said {func_choice}")