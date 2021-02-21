#Kerem Kok
#2/21/2021
#Problem 1. Using for and random.randrange statements to get random integers between 25 and 35
>>> import random
>>> random_list = []
>>> #lenght of the list is 10 for 10 integers
>>> for i in range(0,10):
	#random integers between 25 and 35
	random_list.append(random.randrange(25, 35))
	print(random_list)

	
[31]
[31, 29]
[31, 29, 27]
[31, 29, 27, 29]
[31, 29, 27, 29, 33]
[31, 29, 27, 29, 33, 28]
[31, 29, 27, 29, 33, 28, 28]
[31, 29, 27, 29, 33, 28, 28, 27]
[31, 29, 27, 29, 33, 28, 28, 27, 32]
[31, 29, 27, 29, 33, 28, 28, 27, 32, 32]
>>> 
