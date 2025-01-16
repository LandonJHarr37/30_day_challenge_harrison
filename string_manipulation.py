'''
using split, capitalize, and some substring tricks, manipulate user inputed
strings

Author: Landon Harrison
Version: 01/16/2025
'''

#take the users input of their first, last, and middle name
user_name = input("\nPlease input your first last and middle name: \n   ")

#splits the name of the user into a list of words 
f_l_m_initials = user_name.split(" ")

#prints the names as a list 
print(f_l_m_initials, "\n")

#iterates throught the list and prints the initials capitalized seperated by periods
for name in f_l_m_initials:
    #prints the initials in the same line, capitalized and followed by a .
    #the end= "" ensures that a new line is not inserted after the initials 
    print(f"{name[0:1].capitalize()}.", end= "") 

reversed = input("\nGive me a random wacky sentence: \n  ")

# the colons: start:end:steps, this denotes that we are printing one character at a time
# backwards, until there are no characters left
print("\n", reversed[::-1])