Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/21/2021
>>> #Problem 5. Converting radians into degrees.
>>> import math
>>> def degree(x):
	#define the value of pi
	pi=math.pi
	#calculation for the conversion
	degree=(x*180)/pi
	return degree

>>> print("Value in Degree:",degree(1.5))
Value in Degree: 85.94366926962348
>>> 