# The list of candies to print to the screen
candylist = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]


# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

for candy in candylist:
	print("[" + str(candylist.index(candy)) +"]" +candy)

for x in range(allowance):
	selected = input("Which candy would you like ot bring home? ")

	candyCart.append(candylist[int(selected)])

print("I brought home with me...")
for candy in candyCart:
	print(candy)