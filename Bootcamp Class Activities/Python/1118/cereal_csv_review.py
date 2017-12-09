import os
import csv


name = []
fiber = []

with open(cereal_bonus_csv, newLine="") as csvfile:
	csvreader= csv.reader(csvfile, delimiter=",")
for row in csvreader:

	if float(row[7]) >= 5:
	print(row)
