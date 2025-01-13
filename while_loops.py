'''
This class implements while loops, used for cases where the writer is unsure how many times a loop should run
    quits after a condition is met

prints counter from 1 - 10
prompts for username until "quit" is given 

Author: Landon Harrison
Version: 1/13/2025
'''

#runs 10 times, initial test of while loop
print() # for formatting
counter = 0
while counter <= 10:
    print(f"counter is now: {counter}")
    counter +=1

print() # for formatting

#test of execute once condition is met, until user types quit, will prompt for user name 
name = ""
counter = 1
while name != "quit":
    name = input("Enter your username: ")
    name = name.strip()

    #prints user name and user number (number increments every input)
    if(name != "quit"):
        print(f"Hi user {counter}: {name}")
        counter +=1
    else:
        print("Okay bye!")