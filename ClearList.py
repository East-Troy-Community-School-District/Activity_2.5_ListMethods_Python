'''
Clear List
Pawelski
3/28/2023
Python I

Instructions:
Predict what the program will display in
the console. Record your prediction on
the provided activity sheet. Check your
prediction by running the program.
'''

cities = ["East Troy"]
cities.append("Milwaukee")
cities.clear()
cities.append("Madison")
cities.append("Stevens Point")
cities.insert(0, "Green Bay")
cities.remove("Madison")
cities.insert(1, "Portage")
cities.pop(2)
print(cities)