import numpy as np
import pandas as pd
import random
import datetime
from tkinter import *


# Make a window to display GUI data
window = Tk()
window.title("Meal Planner")
window.geometry('800x450')


# Get current time time stamp
timeStamp = str(datetime.datetime.now().strftime("%Y-%m-%d"))


# Read in CSV file of meal data
mealData = pd.read_csv('meals.csv',
            header = None,
            names = ['MAIN'])

sideData = pd.read_csv('sides.csv',
            header = None,
            names = ['SIDES'])


# Process data, make two unique lists, and shuffle the order
mains = mealData.MAIN.dropna()
mains = list(set(mains))
random.shuffle(mains)

sides = sideData.SIDES.dropna()
sides = list(set(sides))
random.shuffle(sides)


# Read in CSV file of data
weeklyData = pd.read_csv('weeklyData.csv',
            header = 0,
            names = ['Date', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])


# Put the days of the week in the GUI
daysOfWeek = ['  Monday  ', '  Tuesday  ', '  Wednesday  ', '  Thursday  ', '  Friday  ', '  Saturday  ', '  Sunday  ']

for i in range(len(daysOfWeek)):
    lbl = Label(window, text=daysOfWeek[i], font=("Arial Bold", 20))
    lbl.grid(column=i, row=0)


# Display the last 4 weeks
rowIdx = 1
columnIdx = 0

for i in range(-4,0,1):
    for j in range(1,8,1):
        out = weeklyData.iat[i,j]

        b = Label(window, anchor="w", text=out, font=("Arial", 14))
        b.grid(row=rowIdx, column=columnIdx)
        #b.grid(row=rowIdx, column=columnIdx, sticky="w")
        columnIdx += 1

    rowIdx += 1
    columnIdx = 0


# Add some white space in GUI
lbl = Label(window, text=""); lbl.grid(column=0, row=8)
lbl = Label(window, text=""); lbl.grid(column=0, row=9)


# Find this weeks meals and place in the GUI
fields = [mains[0], mains[1], mains[2], mains[3], mains[4], mains[5], mains[6]]

daysOfWeek = ['  Monday  ', '  Tuesday  ', '  Wednesday  ', '  Thursday  ', '  Friday  ', '  Saturday  ', '  Sunday  ']

for i in range(len(daysOfWeek)):
    lbl = Label(window, text=daysOfWeek[i], font=("Arial Bold", 20))
    lbl2 = Label(window, text=fields[i], font=("Arial", 14))
    lbl.grid(column=i, row=10)
    lbl2.grid(column=i, row=11)


# Define buttons for changing a meal
counter = 6

def clicked0():
    global counter
    counter += 1
    fields[0] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=0, row=11)
    lbl = Label(window, text=fields[0], font=("Arial", 14))
    lbl.grid(column=0, row=11)

def clicked1():
    global counter
    counter += 1
    fields[1] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=1, row=11)
    lbl = Label(window, text=fields[1], font=("Arial", 14))
    lbl.grid(column=1, row=11)

def clicked2():
    global counter
    counter += 1
    fields[2] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=2, row=11)
    lbl = Label(window, text=fields[2], font=("Arial", 14))
    lbl.grid(column=2, row=11)

def clicked3():
    global counter
    counter += 1
    fields[3] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=3, row=11)
    lbl = Label(window, text=fields[3], font=("Arial", 14))
    lbl.grid(column=3, row=11)

def clicked4():
    global counter
    counter += 1
    fields[4] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=4, row=11)
    lbl = Label(window, text=fields[4], font=("Arial", 14))
    lbl.grid(column=4, row=11)

def clicked5():
    global counter
    counter += 1
    fields[5] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=5, row=11)
    lbl = Label(window, text=fields[5], font=("Arial", 14))
    lbl.grid(column=5, row=11)

def clicked6():
    global counter
    counter += 1
    fields[6] = mains[counter]
    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=6, row=11)
    lbl = Label(window, text=fields[6], font=("Arial", 14))
    lbl.grid(column=6, row=11)


btn = Button(window, text="Change", command=clicked0); btn.grid(column=0, row=12)
btn = Button(window, text="Change", command=clicked1); btn.grid(column=1, row=12)
btn = Button(window, text="Change", command=clicked2); btn.grid(column=2, row=12)
btn = Button(window, text="Change", command=clicked3); btn.grid(column=3, row=12)
btn = Button(window, text="Change", command=clicked4); btn.grid(column=4, row=12)
btn = Button(window, text="Change", command=clicked5); btn.grid(column=5, row=12)
btn = Button(window, text="Change", command=clicked6); btn.grid(column=6, row=12)


# Add some white space in GUI
lbl = Label(window, text=""); lbl.grid(column=0, row=13)


# Add swapping two days of meals
lbl = Label(window, text="Swap day"); lbl.grid(column=0, row=14, sticky="e")
lbl = Label(window, text="   Enter days to swap E.g. Monday = 1, Tuesday = 2 ... Sunday = 7"); lbl.grid(column=2, row=14, columnspan=4, sticky="w")
lbl = Label(window, text="with"); lbl.grid(column=0, row=15, sticky="e")

pos1 = Entry(window,width=10); pos1.grid(column=1, row=14)
pos2 = Entry(window,width=10); pos2.grid(column=1, row=15)

def swap():
    idx1 = int(pos1.get())-1
    idx2 = int(pos2.get())-1
    fields[idx1], fields[idx2] = fields[idx2], fields[idx1]

    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=idx1, row=11)
    lbl = Label(window, text=fields[idx1], font=("Arial", 14))
    lbl.grid(column=idx1, row=11)

    lbl = Label(window, text="\t\t", bg="white"); lbl.grid(column=idx2, row=11)
    lbl = Label(window, text=fields[idx2], font=("Arial", 14))
    lbl.grid(column=idx2, row=11)

    pos1.delete(0,END)
    pos2.delete(0,END)

btn = Button(window, text="Execute", command=swap)
btn.grid(column=1, row=16)


# Add some white space in GUI
lbl = Label(window, text=""); lbl.grid(column=0, row=17)
lbl = Label(window, text=""); lbl.grid(column=0, row=18)


# Save the data and exit
def saveAndExit():
    global timeStamp
    global fields
    fields.insert(0, timeStamp)

    newData = pd.DataFrame(columns=['Date','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    newData.loc[weeklyData.tail(1).index.item()+1] = fields

    with open('weeklyData.csv', 'a') as f:
        newData.to_csv(f, header=False, index=False)

    window.destroy()


btn = Button(window, text="Save and Exit", command=saveAndExit)
btn.grid(column=3, row=19)

# Run forever until destroyed
window.mainloop()
