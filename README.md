# Automated Meal Planning
Automated meal planner showing previous four weeks of meals and provides randomized suggestions for this weeks meals and sides. Graphical user interface (GUI) provides options for swapping and further randomizing meals and sides. Ingredients are shown for the current meal and side selection.  

## Set Up on macOS
macOS comes preinstalled with python and some basic packages and modules. To use the automated meal planner some additional packages and updates must be installed. Complete the following:

* Install [python3](https://www.python.org/downloads/)
* Press "command" and "space bar" at the same time and type "Terminal" (without the quotes) then enter:

```
pip3 install pandas
```

## Running Program on macOS
Using terminal navigate to the directory (folder) where the "mealPlanner.py" file is located. For example:
```
cd /Users/MarkSherstan/Desktop/Meal-Planning
```

You may also type cd in the terminal window and drag and drop the folder into the terminal window to get the path.

To run the program enter:
```
python3 mealPlanner.py
```

Or double click on the "Meal Planner" icon (ensure that the .csv files are located in the same directory or folder).

## Adding Meals and Sides or Editing Previous Data
To add additional meals or sides edit the meals.csv or sides.csv following the same format as in the current files. Text is case sensitive and must be consistent. To edit a previous week edit the weeklyData.csv as desired.

## Sample App Output
![Text goes here](https://i.ibb.co/5MWQTD7/git-Hub-Meal-Planner-Photo.png)
