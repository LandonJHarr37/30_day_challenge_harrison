'''
This class implements for loops, to "automate the boring stuff"

Author: Landon Harrison
Version: 1/12/2025
'''

fav_fruits = ["mangos", "sour blueberries", "pears", "oranges"]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_cubed = []

#printing my favorite fruits using a for loop
counter = 1
print() # for pretty formatting(an empty line above first fruit)
for fruit in fav_fruits:
    print(f"fruit number {counter}: {fruit}\n")
    counter +=1

#reassigning the cubes of each num in nums to the spot of the original in nums
print(f"Nums: \n{nums}")
print("Cubed nums: ")
for num in nums:
    nums_cubed.append(num * num * num)
print(nums_cubed) #printing the new list of nums