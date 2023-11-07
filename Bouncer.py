'''
Bouncer
Pawelski
11/6/2023
Introduction to Computer Science

Instructions:
What does this program do?
Read the code and run the program to see!
You may want to step through the program one
line at a time to see what each line does
individually. Finally, modify the program so
that you are on the bouncer's list.
'''

guests = ["Jimbo", "Jimbob", "Jenny", "Jennifer", "Jen", "Jim"]
while len(guests) > 0:
    name = input("Enter a name to check if it is on the list >> ")
    if name in guests:
        print("Welcome, you are on the list.")
        guests.pop(guests.index(name))
    else:
        print("Stop! You are not on the list.")
    print()
print("Everyone is here!")