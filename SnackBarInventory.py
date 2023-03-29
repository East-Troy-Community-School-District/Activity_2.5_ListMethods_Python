'''
Snack Bar Inventory
Pawelski
3/28/2023
Python I

Instructions:
What does this program do? Read the code and
run the program to see!
'''

inventory = []
option = 1
while option != 4:
    print("What would you like to do?")
    print("1. View the inventory.")
    print("2. Add an item to the inventory.")
    print("3. Remove an item from the inventory.")
    print("4. Exit the program.")
    option = int(input("Enter your option (1-4) >> "))
    print()

    if option == 1:
        print(inventory)
    elif option == 2:
        item = input("Enter the item to add >> ").lower()
        inventory.append(item)
        inventory.sort()
    elif option == 3:
        item = input("Enter the item to remove >> ").lower()
        if item in inventory:
            inventory.remove(item)
        else:
            print("No item matches that in the inventory.")
    elif option != 4:
        print("Invalid option!")
    print()
