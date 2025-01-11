'''
experiment with variables (and formatting of print statements ): talking about my dog
variable: labeled box where you can store contents, tend to store a certain "shape"
    or type of content. Used to call upon data or change it.

Author: Landon Harrison
Version: 01/10/2025
'''

dog_name = "Archer"
dog_age = 4

print("\nmy dog is named", dog_name, "and she is", str(dog_age), "years old.\n")

dog_age +=1 #archer turns 5, happy barkday

print(f"{dog_name} just turned {dog_age}, woohoo. \n")

dog_toy = "bone"
dog_weight = 115
dog_treat = "chicken"

print(f"{dog_name} gets {dog_treat} when she is good, enjoys "\
      f"{dog_toy}s, and weighs {dog_weight} lbs.\n")
