Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/21/2021
>>> #Problem 6. Using for loop to calculate the factorial of number 4.
>>> import math
>>> num = int(input("enter a number: "))
enter a number: 4
>>> #entered number 4
>>> fac = 1
>>> for i in range(1, num +1):
	fac = fac * i #formula to calculate factorial

	
>>> print("factorial of ", num, " is ", fac)
factorial of  4  is  24
>>> 