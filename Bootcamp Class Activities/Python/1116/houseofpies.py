print("Welcome to the House of Pies! Here are our pies:")
pielist = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
for pie in pielist:
	print("(" + str(pielist.index(pie)+1) + ") " +pie +" ", end='')

choice = int(input("\nWhich would you like? (Enter a number)")) 
print("\nGreat! We'll have that " + pie +" right out for you.")
