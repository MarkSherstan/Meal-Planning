# Automated Meal Planning
Automated meal planner showing previous four weeks of meals and provides randomized suggestions for the current weeks meals and sides. Graphical user interface (GUI) provides options for swapping and further randomizing meals and sides. Ingredients are shown for the current meal and side selection.  

## macOS Users
macOS comes preinstalled with python and some basic packages and modules. To use the automated meal planner additional packages and updates must be installed. Complete the following:

* Download or clone meal planning files (green button at top of page)
* Install [python3](https://www.python.org/downloads/)
* Press "command" and "space bar" at the same time and type "Terminal" (without the quotes) and open the terminal app. In the terminal window enter:
```
pip3 install pandas
```

Using terminal navigate to the directory (folder) where the "mealPlanner.py" file is located. You may also type cd in the terminal window and drag and drop the folder into the terminal window to get the path. For example:
```
cd /Users/MarkSherstan/Desktop/Meal-Planning
```

To run the program enter:
```
python3 mealPlanner.py
```

## Windows Users
Follow macOS instructions and make sure that Python is added to PATH at the start of the installer. Instead of terminal use cmd.exe (find using Windows search). Assuming a clean install the following must be entered in the command line:
```
pip install pandas
```

Navigate to the correct folder in the command line using the same process as macOS. For Example:
```
cd "C:\Users\Mark Sherstan\Desktop\Meal-Planning"
```

To run the program enter:
```
python mealPlanner.py
```

## Usage Notes
The recommended technique(s) are just one of many ways to run the program. As long as the .csv files and .py file are in the same folder other options are available (e.g. - IDLE).

## Adding Meals and Sides or Editing Previous Data
To add additional meals or sides edit the meals.csv or sides.csv following the same format as in the current files. Text is case sensitive and must be consistent. To edit a previous week edit the weeklyData.csv as desired.

## Program Screenshot
![Text goes here](https://i.ibb.co/5MWQTD7/git-Hub-Meal-Planner-Photo.png)
