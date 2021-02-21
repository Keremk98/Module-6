Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Kerem Kok
>>> #2/21/2021
>>> #Problem 3. Selecting a day of the week from a list and printing that day.
>>> import random
>>> days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
>>> #picking a random choice from the list.
>>> day = random.choice(days_list)
>>> print(day)
Friday
>>> 