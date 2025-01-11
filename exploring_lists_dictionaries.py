'''
This class implements lists and dictionaries to learn how they work

Author: Landon Harrison
Version: 1/11/2025
'''

''' lists '''
# dog names in my house right now 
# enclosed in square brackets and seperated by comments 
our_dogs = ["Archer", "Jazzy", "Charlese", "Maggie"]

#zero-indexed, for the first item use 0 as index
print()
print(our_dogs)
print()
print(our_dogs[0])
print()

#you can append, remove, or change items 
our_dogs.append("raegan")
save_dog = our_dogs[2] #saving third dog in a variable to fix alphabetical order of list
our_dogs[2] = our_dogs[1] #replacing third dog with second dog
our_dogs[1] = save_dog #putting the saved dog in slot two
our_dogs.remove("Maggie")

#prints the new list of dogs after appending raegan, switching Jazzy and Charlese, and removing Maggie
print(f"New list of dogs after appending raegan, switching Jazzy and Charlese, and removing Maggie: \n{our_dogs}")
print()

'''Dictionaries'''
#information about oldest dog
#keys paired with information, curly brackets, seperated by commas, and formatting key : info
oldest_dog = {"name": "Jazzy", "age": 8, "color": "white", "spots": "orange"}
print(f"my oldest dog named {oldest_dog['name']}: {oldest_dog}")
print()

oldest_dog['age'] = 9 #changing Jazzy's age

print(f"{oldest_dog['name']} turned {oldest_dog['age']}: {oldest_dog}")
print()

oldest_dog['new_spots'] = "blue" # adding new spots after abduction

print(f"{oldest_dog['name']} is abducted by aliens and {oldest_dog['new_spots']} spots show up: \n{oldest_dog}")
print()

del oldest_dog["new_spots"] 

print(f"Jazzy got her new spots died orange: {oldest_dog}")
print()

