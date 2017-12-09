import os
import csv

video = input("What would you like to search for?")

csvpath = os.path.join('netflix_ratings.csv')


with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	for row in csvreader:
		if row[0] == video:
			print(row[0] + " is rated " + row[1] + " with a rating of " + row[6])

			found = True
	if found == False:
		print("Sorry about this, we don't seem to have what you're looking for.")
