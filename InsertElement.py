'''
Insert Element
Pawelski
3/28/2023
Python II

Instructions:
Predict what the program will display in
the console. Record your prediction on
the provided activity sheet. Check your
prediction by running the program. 

In addition, modify this program by having
it insert the color "cyan" at the very
beginning of the list (don't just add it
in the brackets [], use the insert() method).
Check your work by having it print the list
the console.
'''

colors = ["white"]
colors.append("red")
colors.append("green")
colors.append("blue")
colors.insert(1, "black")
colors.append("yellow")
colors.insert(2, "brown")
print(colors)
