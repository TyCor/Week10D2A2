#In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chicken = 2 
cow = 4 
dog = 4

#The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a script or function that returns the total number of legs of all the animals.

def animals(chicken_leg, cow_leg, dog_leg):
	leg1 = chicken*chicken_leg
	leg2 = cow * cow_leg
	leg3 = dog * dog_leg
	all_legs = leg1 + leg2 + leg3
	return all_legs   

#Example 1
print(animals(2, 3, 5))

#Example 2
#input(1, 2, 3) ➞ 22

#Example 3
#How many Chickens? 5
#How many Cows? 2
#How many Dogs? 8
#50 legs

#Create a python script to solve this problem.
