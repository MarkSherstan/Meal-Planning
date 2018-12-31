import numpy as np
import pandas as pd
import random
import datetime
import tkinter
from tkinter import *
from tkinter import ttk


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
monday.set(mains[0])
w = OptionMenu(window, monday, *sorted(mains))
w.grid(column=0, row=11, sticky="ew")

tuesday = StringVar(window)
tuesday.set(mains[1])
w = OptionMenu(window, tuesday, *sorted(mains))
w.grid(column=1, row=11, sticky="ew")

wednesday = StringVar(window)
wednesday.set(mains[2])
w = OptionMenu(window, wednesday, *sorted(mains))
w.grid(column=2, row=11, sticky="ew")

thursday = StringVar(window)
thursday.set(mains[3])
w = OptionMenu(window, thursday, *sorted(mains))
w.grid(column=3, row=11, sticky="ew")

friday = StringVar(window)
friday.set(mains[4])
w = OptionMenu(window, friday, *sorted(mains))
w.grid(column=4, row=11, sticky="ew")

saturday = StringVar(window)
saturday.set(mains[5])
w = OptionMenu(window, saturday, *sorted(mains))
w.grid(column=5, row=11, sticky="ew")

sunday = StringVar(window)
sunday.set(mains[6])
w = OptionMenu(window, sunday, *sorted(mains))
w.grid(column=6, row=11, sticky="ew")


# Set up style for buttons
windowBgColor = window.cget("background")

style = ttk.Style()
style.theme_use('default')

style.configure('TCheckbutton',
                background=windowBgColor,
                foreground=windowBgColor,
                focuscolor=windowBgColor)

style.configure('TCheckbutton',selectcolor="green")

style.map('TCheckbutton',
        foreground=[('disabled', windowBgColor),
                    ('pressed', windowBgColor),
                    ('active', windowBgColor)],
        background=[('disabled', windowBgColor),
                    ('pressed', '!focus', windowBgColor),
                    ('active', windowBgColor)],
        highlightcolor=[('focus', windowBgColor),
                        ('!focus', windowBgColor)],
        relief=[('pressed', 'groove'),
                ('!pressed', 'ridge')])


# Add check boxes for swapping days
def check():
    checkBoxes = [chk0.instate(['selected']), chk1.instate(['selected']),
                  chk2.instate(['selected']), chk3.instate(['selected']),
                  chk4.instate(['selected']), chk5.instate(['selected']),
                  chk6.instate(['selected'])]

    if sum(checkBoxes) == 2:
        for i in range(len(checkBoxes)):
            if globals()['chk' + str(i)].instate(['selected']) == False:
                globals()['chk' + str(i)].state(['disabled'])
    else:
        for i in range(len(checkBoxes)):
            globals()['chk' + str(i)].state(['!disabled'])



chk0 = ttk.Checkbutton(window, command=check)
chk0.state(['!alternate','!selected'])
chk0.grid(column=0, row=12)

chk1 = ttk.Checkbutton(window, command=check)
chk1.state(['!alternate','!selected'])
chk1.grid(column=1, row=12)

chk2 = ttk.Checkbutton(window, command=check)
chk2.state(['!alternate','!selected'])
chk2.grid(column=2, row=12)

chk3 = ttk.Checkbutton(window, command=check)
chk3.state(['!alternate','!selected'])
chk3.grid(column=3, row=12)

chk4 = ttk.Checkbutton(window, command=check)
chk4.state(['!alternate','!selected'])
chk4.grid(column=4, row=12)

chk5 = ttk.Checkbutton(window, command=check)
chk5.state(['!alternate','!selected'])
chk5.grid(column=5, row=12)

chk6 = ttk.Checkbutton(window, command=check)
chk6.state(['!alternate','!selected'])
chk6.grid(column=6, row=12)


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

btn = Button(window, text="Randomize", command=clicked0); btn.grid(column=0, row=13)
btn = Button(window, text="Randomize", command=clicked1); btn.grid(column=1, row=13)
btn = Button(window, text="Randomize", command=clicked2); btn.grid(column=2, row=13)
btn = Button(window, text="Randomize", command=clicked3); btn.grid(column=3, row=13)
btn = Button(window, text="Randomize", command=clicked4); btn.grid(column=4, row=13)
btn = Button(window, text="Randomize", command=clicked5); btn.grid(column=5, row=13)
btn = Button(window, text="Randomize", command=clicked6); btn.grid(column=6, row=13)


# Add some white space in GUI
lbl = Label(window, text=""); lbl.grid(column=0, row=14)
lbl = Label(window, text=""); lbl.grid(column=0, row=15)

# Swap days
def swap():
    checkBoxes = [chk0.instate(['selected']), chk1.instate(['selected']),
                  chk2.instate(['selected']), chk3.instate(['selected']),
                  chk4.instate(['selected']), chk5.instate(['selected']),
                  chk6.instate(['selected'])]

    currentMeals = [monday.get(), tuesday.get(), wednesday.get(), thursday.get(), friday.get(), saturday.get(), sunday.get()]

    swapIdx = np.where(checkBoxes)

    if len(swapIdx[0]) == 2:
        currentMeals[swapIdx[0][0]], currentMeals[swapIdx[0][1]] = currentMeals[swapIdx[0][1]], currentMeals[swapIdx[0][0]]

        monday.set(currentMeals[0])
        tuesday.set(currentMeals[1])
        wednesday.set(currentMeals[2])
        thursday.set(currentMeals[3])
        friday.set(currentMeals[4])
        saturday.set(currentMeals[5])
        sunday.set(currentMeals[6])

        # Clear the checkboxes and enable them all again
        for i in range(7):
            globals()['chk' + str(i)].state(['!disabled','!selected'])


btn = Button(window, text="Swap 2 Meals", command=swap)
btn.grid(column=1, row=16)

btn = Button(window, text="Swap 2 Sides", command=swap)
btn.grid(column=5, row=16)


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
