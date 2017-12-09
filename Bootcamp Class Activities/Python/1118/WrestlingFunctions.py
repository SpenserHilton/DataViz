import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join("WWE-Data-2016.csv")
# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(row):
    
    wins = int(row[1])
    losses = int(row[2])
    draws = int(row[3])
    
    # Find the total number of matches wrestled
    total = wins+losses+draws
    # Find the percentage of matches won
    percwin = float(wins/total)
    # Find the percentage of matches lost
    percloss = float(losses/total)
    # Find the percentage of matches drawn
    percdraw = float(draws/total)
    # Print out the wrestler's name and their percentage stats
    print(row[0],"won"+ percwin,"%", "lost" +percloss,"%", "and drew" +percdraw,"of his" + total,"matches.")
# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")
    # Loop through the data
    for row in csvreader:
        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)


SOLVED




import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join('..','Resources','WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(wrestlerData):
    
    # Total matches can be found by adding wins, losses, and draws together
    totalMatches = int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])
    wins = int(wrestlerData[1])
    losses = int(wrestlerData[2])
    draws = int(wrestlerData[3]) 
    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    winPercent = (wins/totalMatches)*100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    lossPercent = (losses/totalMatches)*100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    drawPercent = (draws/totalMatches)*100

    # If the loss percentage is over 50, typeOfWrestler is "Jobber". Otherwise it is "Superstar".
    if(lossPercent > 50):
        typeOfWrestler = "Jobber"
    else:
        typeOfWrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print("Stats for " + wrestlerData[0])
    print("WIN PERCENT: " + str(winPercent))
    print("LOSS PERCENT: " + str(lossPercent))
    print("DRAW PERCENT: " + str(drawPercent))
    print(wrestlerData[0] + " is a " + typeOfWrestler)

# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")
    
    # Loop through the data
    for row in csvreader:
        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)