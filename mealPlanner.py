import numpy as np
import pandas as pd
import random
import datetime


# Get current time time stamp
timeStamp = str(datetime.datetime.now().strftime("%Y-%m-%d"))


# Read in CSV file of meal data
mealData = pd.read_csv('meals.csv',
            header = -1, # is this right???
            names = ['MAIN','SIDE'])


# Process data, make two unique lists, and shuffle the order
mains = mealData.MAIN.dropna()
mains = list(set(mains))
random.shuffle(mains)

sides = mealData.SIDE.dropna()
sides = list(set(sides))
random.shuffle(sides)


# Read in CSV file of data
weeklyData = pd.read_csv('weeklyData.csv',
            header = 0,
            names = ['Date', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])


# Print the last 4 weeks
print('\nLast months meals:')
print('____________________\n')
print(weeklyData.iloc[-4:])
print


# Print the initial results
fields = [timeStamp, mains[0], mains[1], mains[2], mains[3], mains[4], mains[5], mains[6]]
newData = pd.DataFrame(columns=['Date','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
newData.loc[weeklyData.tail(1).index.item()+1] = fields

print('\nThis weeks meals:')
print('____________________\n')
print(newData)
print


# Print the instructions
print('_______________________________________________________')
print('If happy with the data press enter\n')
print('To change a meal, enter the numeric day of the week:')
print('    E.g. Monday = 1, Tuesday = 2 ... Sunday = 7\n')
print('To swap two days enter "swap" and follow the directions')
print('_______________________________________________________')


# Procces the input
userInput = raw_input("\nEnter your response: ")
counter = 7

while userInput != "":

    if userInput == "swap":
        pos1 = input("Swap day: ")
        pos2 = input("for day: ")
        fields[pos1], fields[pos2] = fields[pos2], fields[pos1]
        counter = counter - 1
    elif int(userInput) == 1:
        fields[1] = mains[counter]
    elif int(userInput) == 2:
        fields[2] = mains[counter]
    elif int(userInput) == 3:
        fields[3] = mains[counter]
    elif int(userInput) == 4:
        fields[4] = mains[counter]
    elif int(userInput) == 5:
        fields[5] = mains[counter]
    elif int(userInput) == 6:
        fields[6] = mains[counter]
    elif int(userInput) == 7:
        fields[7] = mains[counter]
    else:
        print("Incorrect Entry")
        counter = counter - 1

    if counter == len(mains)-1:
        print("Out of meal options")
        break

    print
    newData = pd.DataFrame(columns=['Date','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    newData.loc[weeklyData.tail(1).index.item()+1] = fields
    print(newData)
    print

    counter = counter + 1
    userInput = raw_input("Enter your response: ")


# Merge the new data with the previous data
result = weeklyData.append(newData)


# Save results to csv file
with open('weeklyData.csv', 'a') as f:
    newData.to_csv(f, header=False, index=False)
