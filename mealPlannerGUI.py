import numpy as np
import pandas as pd
import random
import datetime
from tkinter import *


# Make a window to display GUI data
window = Tk()
window.title("Meal Planner")
window.geometry('975x450')


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
daysOfWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(len(daysOfWeek)):
    lbl = Label(window, text=daysOfWeek[i], width=12, font=("Arial Bold", 20))
    lbl.grid(column=i, row=0)


# Display the last 4 weeks
rowIdx = 1
columnIdx = 0

for i in range(-4,0,1):
    for j in range(1,8,1):
        out = weeklyData.iat[i,j]

        b = Label(window, anchor="w", text=out, font=("Arial", 14))
        b.grid(row=rowIdx, column=columnIdx)
        columnIdx += 1

    rowIdx += 1
    columnIdx = 0


# Add some white space in GUI and add the days of the week again
lbl = Label(window, text=""); lbl.grid(column=0, row=8)
lbl = Label(window, text=""); lbl.grid(column=0, row=9)


for i in range(len(daysOfWeek)):
    lbl = Label(window, text=daysOfWeek[i], font=("Arial Bold", 20))
    lbl.grid(column=i, row=10)


# Drop down selectors
monday = StringVar(window)
monday.set(mains[0]) # default value
w = OptionMenu(window, monday, *sorted(mains))
w.grid(column=0, row=11, sticky="ew")

tuesday = StringVar(window)
tuesday.set(mains[1]) # default value
w = OptionMenu(window, tuesday, *sorted(mains))
w.grid(column=1, row=11, sticky="ew")

wednesday = StringVar(window)
wednesday.set(mains[2]) # default value
w = OptionMenu(window, wednesday, *sorted(mains))
w.grid(column=2, row=11, sticky="ew")

thursday = StringVar(window)
thursday.set(mains[3]) # default value
w = OptionMenu(window, thursday, *sorted(mains))
w.grid(column=3, row=11, sticky="ew")

friday = StringVar(window)
friday.set(mains[4]) # default value
w = OptionMenu(window, friday, *sorted(mains))
w.grid(column=4, row=11, sticky="ew")

saturday = StringVar(window)
saturday.set(mains[5]) # default value
w = OptionMenu(window, saturday, *sorted(mains))
w.grid(column=5, row=11, sticky="ew")

sunday = StringVar(window)
sunday.set(mains[6]) # default value
w = OptionMenu(window, sunday, *sorted(mains))
w.grid(column=6, row=11, sticky="ew")


# Define buttons for randomizing a meal
counter = 6

def clicked0():
    global counter
    counter += 1
    monday.set(mains[counter])

def clicked1():
    global counter
    counter += 1
    tuesday.set(mains[counter])

def clicked2():
    global counter
    counter += 1
    wednesday.set(mains[counter])

def clicked3():
    global counter
    counter += 1
    thursday.set(mains[counter])

def clicked4():
    global counter
    counter += 1
    friday.set(mains[counter])

def clicked5():
    global counter
    counter += 1
    saturday.set(mains[counter])

def clicked6():
    global counter
    counter += 1
    sunday.set(mains[counter])

btn = Button(window, text="Randomize", command=clicked0); btn.grid(column=0, row=12)
btn = Button(window, text="Randomize", command=clicked1); btn.grid(column=1, row=12)
btn = Button(window, text="Randomize", command=clicked2); btn.grid(column=2, row=12)
btn = Button(window, text="Randomize", command=clicked3); btn.grid(column=3, row=12)
btn = Button(window, text="Randomize", command=clicked4); btn.grid(column=4, row=12)
btn = Button(window, text="Randomize", command=clicked5); btn.grid(column=5, row=12)
btn = Button(window, text="Randomize", command=clicked6); btn.grid(column=6, row=12)


# Add some white space in GUI
lbl = Label(window, text=""); lbl.grid(column=0, row=13)


# Add swapping two days of meals
lbl = Label(window, text="Swap day"); lbl.grid(column=0, row=14, sticky="e")

lbl = Label(window, text="   Enter days to swap E.g. Monday = 1, Tuesday = 2 ... Sunday = 7");
lbl.grid(column=2, row=14, columnspan=4, sticky="w")

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
    timeStamp = str(datetime.datetime.now().strftime("%Y-%m-%d"))

    fields = [timeStamp, monday.get(), tuesday.get(), wednesday.get(), thursday.get(), friday.get(), saturday.get(), sunday.get()]

    newData = pd.DataFrame(columns=['Date','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    newData.loc[weeklyData.tail(1).index.item()+1] = fields

    with open('weeklyData.csv', 'a') as f:
        newData.to_csv(f, header=False, index=False)

    window.destroy()


btn = Button(window, text="Save and Exit", command=saveAndExit)
btn.grid(column=3, row=19)


# Run forever until destroyed
window.mainloop()
