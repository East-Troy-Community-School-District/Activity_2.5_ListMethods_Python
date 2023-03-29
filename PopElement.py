'''
Pop Element
Pawelski
3/28/2023
Python II

Instructions:
Predict what the program will display in
the console. Record your prediction on
the provided activity sheet. Check your
prediction by running the program. 

Try adding the following line of code to
the program...
artists.pop(25)

This line causes an error. Why? What element
did the following line of code remove from
the list?
artists.pop(len(artists) - 1)
'''

artists = ["Picasso", "Monet", "Warhol", "Vermeer", "Pollock"]
print(artists)

artists.pop(1)
artists.insert(0, "Rembrandt")
artists.pop(len(artists) - 1)
print(artists)
