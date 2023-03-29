'''
Bouncer
Pawelski
3/28/2023
Python I

Instructions:
What does this program do? Read the code and
run the program to see!
'''

guests = ["Jimbo", "Jimbob", "Jenny", "Jennifer", "Jen", "Jim"]
while len(guests) > 0:
    print(guests)
    name = input("Enter a name to check if it is on the list >> ")
    if name in guests:
        print("Welcome, you are on the list.")
        guests.pop(guests.index(name))
    else:
        print("Stop! You are not on the list.")
    print()
print("Everyone is here!")
