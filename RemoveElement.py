'''
Remove Element
Pawelski
3/28/2023
Python I

Instructions:
Predict what the program will display in
the console. Record your prediction on
the provided activity sheet. Check your
prediction by running the program. 

Try adding the following line of code to
the program...
ph_levels.remove(2.3)

This line causes an error. Why? In addition,
modify this program by having it remove
the first occurance of the number 3.9
(don't just remove it in the brackets [],
use the remove() method). Check your work
by having it print the list the console.
'''

ph_levels = [4.5, 4.7, 4.2, 4.2, 4.2, 4.9, 5.1, 3.9, 4.2, 4.5]
print(ph_levels)

ph_levels.remove(5.1)
print(ph_levels)

ph_levels.remove(4.2)
print(ph_levels)
