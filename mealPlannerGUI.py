import numpy as np
import pandas as pd
import random
import datetime
import tkinter
from tkinter import *
from tkinter import ttk, messagebox, scrolledtext


################################################################################
# GUI Set up
################################################################################

# Make a window to display GUI data
window = Tk()
window.title("Meal Planner")
window.geometry('1250x500')


################################################################################
# Reading and processing CSV's
################################################################################

# Read in CSV file of meal data
mealData = pd.read_csv('meals.csv', header = None)

sideData = pd.read_csv('sides.csv', header = None)


# Process data, make two unique lists, and shuffle the order
mains = mealData[mealData.columns[0]].dropna()
mains = list(set(mains))
random.shuffle(mains)

sides = sideData[sideData.columns[0]].dropna()
sides = list(set(sides))
random.shuffle(sides)


# Read in CSV file of data
weeklyData = pd.read_csv('weeklyData.csv',
            header = 0,
            names = ['Date', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])


################################################################################
# First GUI objects - Headers and static csv data
################################################################################

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


################################################################################
# Create drop downs for Mains and Sides
################################################################################

# Drop down selectors for mains
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



# Drop down selectors for sides
mondaySide = StringVar(window)
mondaySide.set(sides[0])
w = OptionMenu(window, mondaySide, *sorted(sides))
w.grid(column=0, row=12, sticky="ew")

tuesdaySide = StringVar(window)
tuesdaySide.set(sides[1])
w = OptionMenu(window, tuesdaySide, *sorted(sides))
w.grid(column=1, row=12, sticky="ew")

wednesdaySide = StringVar(window)
wednesdaySide.set(sides[2])
w = OptionMenu(window, wednesdaySide, *sorted(sides))
w.grid(column=2, row=12, sticky="ew")

thursdaySide = StringVar(window)
thursdaySide.set(sides[3])
w = OptionMenu(window, thursdaySide, *sorted(sides))
w.grid(column=3, row=12, sticky="ew")

fridaySide = StringVar(window)
fridaySide.set(sides[4])
w = OptionMenu(window, fridaySide, *sorted(sides))
w.grid(column=4, row=12, sticky="ew")

saturdaySide = StringVar(window)
saturdaySide.set(sides[5])
w = OptionMenu(window, saturdaySide, *sorted(sides))
w.grid(column=5, row=12, sticky="ew")

sundaySide = StringVar(window)
sundaySide.set(sides[6])
w = OptionMenu(window, sundaySide, *sorted(sides))
w.grid(column=6, row=12, sticky="ew")


################################################################################
# Set up check buttons
################################################################################


# Set up style for buttons
windowBgColor = window.cget("background")

style = ttk.Style()
style.theme_use('default')

style.configure('TCheckbutton',
                background=windowBgColor,
                foreground=windowBgColor,
                focuscolor=windowBgColor)

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


chk0 = ttk.Checkbutton(window)
chk0.state(['!alternate','!selected'])
chk0.grid(column=0, row=13)

chk1 = ttk.Checkbutton(window)
chk1.state(['!alternate','!selected'])
chk1.grid(column=1, row=13)

chk2 = ttk.Checkbutton(window)
chk2.state(['!alternate','!selected'])
chk2.grid(column=2, row=13)

chk3 = ttk.Checkbutton(window)
chk3.state(['!alternate','!selected'])
chk3.grid(column=3, row=13)

chk4 = ttk.Checkbutton(window)
chk4.state(['!alternate','!selected'])
chk4.grid(column=4, row=13)

chk5 = ttk.Checkbutton(window)
chk5.state(['!alternate','!selected'])
chk5.grid(column=5, row=13)

chk6 = ttk.Checkbutton(window)
chk6.state(['!alternate','!selected'])
chk6.grid(column=6, row=13)


################################################################################
# Put ingrediant data here --> this should be a function called on each button press and first instance
################################################################################

# Add some white space in GUI
lbl = Label(window, text="", width=5); lbl.grid(column=7, row=0)

lbl = Label(window, text="Ingredients", font=("Arial Bold", 20));
lbl.grid(column=8, row=0)

txt = scrolledtext.ScrolledText(window,width=20,height=20)
txt.grid(column=8,row=1,rowspan=15)


def dispIngrediants():
    txt.delete('1.0', END)

    currentMeals = [monday.get(), tuesday.get(), wednesday.get(), thursday.get(), friday.get(), saturday.get(), sunday.get()]
    currentSides = [mondaySide.get(), tuesdaySide.get(), wednesdaySide.get(), thursdaySide.get(), fridaySide.get(), saturdaySide.get(), sundaySide.get()]

    ingrediants = []

    for i in range(7):
        mealDataIdx = list(mealData[mealData.columns[0]]).index(currentMeals[i])
        sideDataIdx = list(sideData[sideData.columns[0]]).index(currentSides[i])

        mealIngrediantsNew = list(mealData.iloc[mealDataIdx,1:-1].dropna())
        sideIngrediantsNew = list(sideData.iloc[sideDataIdx,1:-1].dropna())

        ingrediants.append(mealIngrediantsNew)
        ingrediants.append(sideIngrediantsNew)


    ingrediants = list(set(sum(ingrediants, [])))
    ingrediantsSorted = sorted(ingrediants, key=str.lower)

    for i in range(len(ingrediantsSorted)):
        txt.insert(INSERT, ingrediantsSorted[i]+"\n")
        txt.configure(font=("Arial"))


dispIngrediants()

################################################################################
# Define push button functions for swapping meals and sides
################################################################################

# Add some white space in GUI
# lbl = Label(window, text=""); lbl.grid(column=0, row=14)
lbl = Label(window, text=""); lbl.grid(column=0, row=15)

# Swap meals
def swapMeals():
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
    else:
        messagebox.showerror('Error', 'Must select exactly two days in order to swap')


# Swap sides
def swapSides():
    checkBoxes = [chk0.instate(['selected']), chk1.instate(['selected']),
                  chk2.instate(['selected']), chk3.instate(['selected']),
                  chk4.instate(['selected']), chk5.instate(['selected']),
                  chk6.instate(['selected'])]

    currentSides = [mondaySide.get(), tuesdaySide.get(), wednesdaySide.get(), thursdaySide.get(), fridaySide.get(), saturdaySide.get(), sundaySide.get()]

    swapIdx = np.where(checkBoxes)

    if len(swapIdx[0]) == 2:
        currentSides[swapIdx[0][0]], currentSides[swapIdx[0][1]] = currentSides[swapIdx[0][1]], currentSides[swapIdx[0][0]]

        mondaySide.set(currentSides[0])
        tuesdaySide.set(currentSides[1])
        wednesdaySide.set(currentSides[2])
        thursdaySide.set(currentSides[3])
        fridaySide.set(currentSides[4])
        saturdaySide.set(currentSides[5])
        sundaySide.set(currentSides[6])

        # Clear the checkboxes and enable them all again
        for i in range(7):
            globals()['chk' + str(i)].state(['!disabled','!selected'])
    else:
        messagebox.showerror('Error', 'Must select exactly two days in order to swap')


btn = Button(window, text="Swap Meals", command=swapMeals)
btn.grid(column=2, row=16)

btn = Button(window, text="Swap Sides", command=swapSides)
btn.grid(column=6, row=16)


################################################################################
# Define push buttons and functions for randomizing meals
################################################################################
counterMeals = 7
counterSides = 7


def randomizeMeals():
    global counterMeals

    checkBoxes = [chk0.instate(['selected']), chk1.instate(['selected']),
                  chk2.instate(['selected']), chk3.instate(['selected']),
                  chk4.instate(['selected']), chk5.instate(['selected']),
                  chk6.instate(['selected'])]

    dotw = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for i in range(7):
        if checkBoxes[i] == True:

            if counterMeals == len(mains):
                messagebox.showwarning('Warning', 'Used all available meal options, please select manually from drop down list')
                return

            globals()[dotw[i]].set(mains[counterMeals])
            counterMeals += 1

        # Clear the checkboxes and enable them all again
        for i in range(7):
            globals()['chk' + str(i)].state(['!disabled','!selected'])

    dispIngrediants()


def randomizeSides():
    global counterSides

    checkBoxes = [chk0.instate(['selected']), chk1.instate(['selected']),
                  chk2.instate(['selected']), chk3.instate(['selected']),
                  chk4.instate(['selected']), chk5.instate(['selected']),
                  chk6.instate(['selected'])]

    dotwSide = ['mondaySide', 'tuesdaySide', 'wednesdaySide', 'thursdaySide', 'fridaySide', 'saturdaySide', 'sundaySide']

    for i in range(7):
        if checkBoxes[i] == True:

            if counterSides == len(sides):
                messagebox.showwarning('Warning', 'Used all available side options, please select manually from drop down list')
                return

            globals()[dotwSide[i]].set(sides[counterSides])
            counterSides += 1

        # Clear the checkboxes and enable them all again
        for i in range(7):
            globals()['chk' + str(i)].state(['!disabled','!selected'])

    dispIngrediants()


btn = Button(window, text="Randomize Meals", command=randomizeMeals)
btn.grid(column=0, row=16)

btn = Button(window, text="Randomize Sides", command=randomizeSides)
btn.grid(column=4, row=16)



################################################################################
# Save data to csv --> email? and close GUI/function
################################################################################


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


################################################################################
# GUI inf loop
################################################################################

# Run forever until destroyed
window.mainloop()
