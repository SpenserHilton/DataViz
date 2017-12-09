## Info in Dictionaries

### Instructions

'''* Create a dictionary that will store the following:

  * Your name
  * Your age
  * A list of a few of your hobbies
  * A dictionary of a few times you wake up during the week

* Print out your name, how many hobbies you have and a time you get up during the week.'''
hobbybook = {"name": "Spenser Hilton", "age": "23", "hobbies": "books, video games, music, sports", "wakeup": "8"}
wakeuptime = {"monday-saturday": "8 AM", "sunday": "10 AM"}

print("My name is " + hobbybook["name"] + ".")
print("I am " + hobbybook["age"] + " years old.")
print("My hobbies include: " + hobbybook["hobbies"] + ".")
print("During the week, I wake up at " + wakeuptime["monday-saturday"] + ".")