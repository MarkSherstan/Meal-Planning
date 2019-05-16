//
//  ViewController.swift
//  MenuPlanner+
//
//  Created by Mark Sherstan on 2019-01-21.
//  Copyright © 2019 Mark Sherstan. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    // Outlets
    @IBOutlet weak var mondayMeal: NSPopUpButton!
    @IBOutlet weak var tuesdayMeal: NSPopUpButton!
    @IBOutlet weak var wednesdayMeal: NSPopUpButton!
    @IBOutlet weak var thursdayMeal: NSPopUpButton!
    @IBOutlet weak var fridayMeal: NSPopUpButton!
    @IBOutlet weak var saturdayMeal: NSPopUpButton!
    @IBOutlet weak var sundayMeal: NSPopUpButton!
    
    @IBOutlet weak var mondaySide: NSPopUpButton!
    @IBOutlet weak var tuesdaySide: NSPopUpButton!
    @IBOutlet weak var wednesdaySide: NSPopUpButton!
    @IBOutlet weak var thursdaySide: NSPopUpButton!
    @IBOutlet weak var fridaySide: NSPopUpButton!
    @IBOutlet weak var saturdaySide: NSPopUpButton!
    @IBOutlet weak var sundaySide: NSPopUpButton!
    
    @IBOutlet weak var mondayCheckBox: NSButton!
    @IBOutlet weak var tuesdayCheckBox: NSButton!
    @IBOutlet weak var wednesdayCheckBox: NSButton!
    @IBOutlet weak var thursdayCheckBox: NSButton!
    @IBOutlet weak var fridayCheckBox: NSButton!
    @IBOutlet weak var saturdayCheckBox: NSButton!
    @IBOutlet weak var sundayCheckBox: NSButton!
    
    // Load in Meals class
    var m = Meals()

    // Make global counter
    var mealCounter = 7
    var sideCounter = 7
    
    // Do any additional setup after loading the view
    override func viewDidLoad() {
        super.viewDidLoad()

        // Populate the pop up windows with nothing
        setUpPopUpWindows(mains: m.mains, sides: m.sides, idxMains: m.idxMains, idxSides: m.idxSides)
    }
    
    // Update the view, if already loaded
    override var representedObject: Any? {
        didSet {
        }
    }

    
    ////////////////////////////////////////////////////////////////////////////////////////
    // Private Functions
    ////////////////////////////////////////////////////////////////////////////////////////
    
    private func setUpPopUpWindows(mains: Array<String>, sides: Array<String>, idxMains: Array<Int>, idxSides: Array<Int>) {
        // Meals
        mondayMeal.removeAllItems();        mondayMeal.addItems(withTitles: mains)
        tuesdayMeal.removeAllItems();       tuesdayMeal.addItems(withTitles: mains)
        wednesdayMeal.removeAllItems();     wednesdayMeal.addItems(withTitles: mains)
        thursdayMeal.removeAllItems();      thursdayMeal.addItems(withTitles: mains)
        fridayMeal.removeAllItems();        fridayMeal.addItems(withTitles: mains)
        saturdayMeal.removeAllItems();      saturdayMeal.addItems(withTitles: mains)
        sundayMeal.removeAllItems();        sundayMeal.addItems(withTitles: mains)
        
        mondayMeal.selectItem(at: idxMains[0])
        tuesdayMeal.selectItem(at: idxMains[1])
        wednesdayMeal.selectItem(at: idxMains[2])
        thursdayMeal.selectItem(at: idxMains[3])
        fridayMeal.selectItem(at: idxMains[4])
        saturdayMeal.selectItem(at: idxMains[5])
        sundayMeal.selectItem(at: idxMains[6])
        
        // Sides
        mondaySide.removeAllItems();        mondaySide.addItems(withTitles: sides)
        tuesdaySide.removeAllItems();       tuesdaySide.addItems(withTitles: sides)
        wednesdaySide.removeAllItems();     wednesdaySide.addItems(withTitles: sides)
        thursdaySide.removeAllItems();      thursdaySide.addItems(withTitles: sides)
        fridaySide.removeAllItems();        fridaySide.addItems(withTitles: sides)
        saturdaySide.removeAllItems();      saturdaySide.addItems(withTitles: sides)
        sundaySide.removeAllItems();        sundaySide.addItems(withTitles: sides)
        
        mondaySide.selectItem(at: idxSides[0])
        tuesdaySide.selectItem(at: idxSides[1])
        wednesdaySide.selectItem(at: idxSides[2])
        thursdaySide.selectItem(at: idxSides[3])
        fridaySide.selectItem(at: idxSides[4])
        saturdaySide.selectItem(at: idxSides[5])
        sundaySide.selectItem(at: idxSides[6])
    }
    
    private func clearCheckBoxes(){
        mondayCheckBox.state = .off
        tuesdayCheckBox.state = .off
        wednesdayCheckBox.state = .off
        thursdayCheckBox.state = .off
        fridayCheckBox.state = .off
        saturdayCheckBox.state = .off
        sundayCheckBox.state = .off
    }
    
    private func getFilePath() -> String {
        // Get NSOpenPanel
        let dialog = NSOpenPanel();
        
        // Set the parameters
        dialog.title                   = "Choose a .html file";
        dialog.showsResizeIndicator    = true;
        dialog.showsHiddenFiles        = false;
        dialog.canChooseDirectories    = true;
        dialog.canCreateDirectories    = true;
        dialog.allowsMultipleSelection = false;
        dialog.allowedFileTypes        = ["html"];
        
        // Check what the user selected
        if (dialog.runModal() == NSApplication.ModalResponse.OK) {
            
            // Do some URL checks and hopefully return a result
            let result = dialog.url?.path
                if (result != nil) {
                    return result!
                }
            } else {
            
            // User clicked "Cancel" return empty
            let result: String! = ""
            return result
            }
        
        // Something failed in runModal, return empty
        let result: String! = ""
        return result
    }
    
    
    ////////////////////////////////////////////////////////////////////////////////////////
    // Buttons
    ////////////////////////////////////////////////////////////////////////////////////////

    @IBAction func getExternalData(_ sender: Any) {
        // Get the file path
        let path = getFilePath()
        
        // Update meal class with the new data
        m.updateData(filepath: path)
        
        // Re-populate the pop up windows
        setUpPopUpWindows(mains: m.mains, sides: m.sides, idxMains: m.idxMains, idxSides: m.idxSides)
    }
    
    
    @IBAction func randomizeMealsButton(_ sender: Any) {
        // Reference buttons and get check box states
        let arrayOfMealDays = [mondayMeal, tuesdayMeal, wednesdayMeal, thursdayMeal, fridayMeal, saturdayMeal, sundayMeal]

        let buttonResponse = [mondayCheckBox.state.rawValue, tuesdayCheckBox.state.rawValue, wednesdayCheckBox.state.rawValue,
                              thursdayCheckBox.state.rawValue, fridayCheckBox.state.rawValue, saturdayCheckBox.state.rawValue,
                              sundayCheckBox.state.rawValue]
       
        // Set up a counter and begin the loop
        var ii = 0
        for mealz in arrayOfMealDays {
            
            // Check the check box and update accordingly
            if (buttonResponse[ii] == 1){
                
                // Display error if out of randomized meal choices
                if (mealCounter == m.idxMains.count){
                    let alert = NSAlert()
                    alert.messageText = "Out of Random Meal Selections"
                    alert.alertStyle = .warning
                    alert.addButton(withTitle: "OK")
                    alert.addButton(withTitle: "Cancel")
                    alert.runModal()
                    clearCheckBoxes()
                    return
                }
                
                // Update the random main
                mealz?.selectItem(at: m.idxMains[mealCounter])
                mealCounter += 1
            }
            
            // Increase counter
            ii += 1
        }
        
        // Clear all the checkboxes when done
        clearCheckBoxes()
    }
    
    
    @IBAction func swapMealsButton(_ sender: Any) {
        // Reference buttons and get check box states
        let arrayOfMealDays = [mondayMeal, tuesdayMeal, wednesdayMeal, thursdayMeal, fridayMeal, saturdayMeal, sundayMeal]

        let buttonResponse = [mondayCheckBox.state.rawValue, tuesdayCheckBox.state.rawValue, wednesdayCheckBox.state.rawValue,
                              thursdayCheckBox.state.rawValue, fridayCheckBox.state.rawValue, saturdayCheckBox.state.rawValue,
                              sundayCheckBox.state.rawValue]
        
        if (buttonResponse.reduce(0, +) != 2 ) {
            // Display error if not exactly 2 meals are selected
            let alert = NSAlert()
            alert.messageText = "Select Exactly 2 Meals to Swap"
            alert.alertStyle = .warning
            alert.addButton(withTitle: "OK")
            alert.addButton(withTitle: "Cancel")
            alert.runModal()
            clearCheckBoxes()
            return
        } else {
            // Find the 2 days of interest
            let idxA = buttonResponse.firstIndex(of: 1)!
            let idxB = buttonResponse.lastIndex(of: 1)!
            
            // Find index value for specific meal
            let idxC = arrayOfMealDays[idxA]!.indexOfSelectedItem
            let idxD = arrayOfMealDays[idxB]!.indexOfSelectedItem

            // Swap meals
            arrayOfMealDays[idxA]!.selectItem(at: idxD)
            arrayOfMealDays[idxB]!.selectItem(at: idxC)
        }

        // Clear all the checkboxes
        clearCheckBoxes()
    }
    
    
    @IBAction func randomizeSidesButton(_ sender: Any) {
        // Reference buttons and get check box states
        let arrayOfSideDays = [mondaySide, tuesdaySide, wednesdaySide, thursdaySide, fridaySide, saturdaySide, sundaySide]
        
        let buttonResponse = [mondayCheckBox.state.rawValue, tuesdayCheckBox.state.rawValue, wednesdayCheckBox.state.rawValue,
                              thursdayCheckBox.state.rawValue, fridayCheckBox.state.rawValue, saturdayCheckBox.state.rawValue,
                              sundayCheckBox.state.rawValue]
        
        // Set up a counter and begin the loop
        var ii = 0
        for sidez in arrayOfSideDays {
            
            // Check the check box and update accordingly
            if (buttonResponse[ii] == 1){
                
                // Display error if out of randomized side choices
                if (sideCounter == m.idxSides.count){
                    let alert = NSAlert()
                    alert.messageText = "Out of Random Side Selections"
                    alert.alertStyle = .warning
                    alert.addButton(withTitle: "OK")
                    alert.addButton(withTitle: "Cancel")
                    alert.runModal()
                    clearCheckBoxes()
                    return
                }
                
                // Update the random side
                sidez?.selectItem(at: m.idxSides[sideCounter])
                sideCounter += 1
            }
            
            // Increase counter
            ii += 1
        }
        
        // Clear all the checkboxes when done
        clearCheckBoxes()
    }
    
    
    @IBAction func swapSidesButton(_ sender: Any) {
        // Reference buttons and get check box states
        let arrayOfSideDays = [mondaySide, tuesdaySide, wednesdaySide, thursdaySide, fridaySide, saturdaySide, sundaySide]
        
        let buttonResponse = [mondayCheckBox.state.rawValue, tuesdayCheckBox.state.rawValue, wednesdayCheckBox.state.rawValue,
                              thursdayCheckBox.state.rawValue, fridayCheckBox.state.rawValue, saturdayCheckBox.state.rawValue,
                              sundayCheckBox.state.rawValue]
        
        if (buttonResponse.reduce(0, +) != 2 ) {
            // Display error if not exactly 2 sides are selected
            let alert = NSAlert()
            alert.messageText = "Select Exactly 2 Sides to Swap"
            alert.alertStyle = .warning
            alert.addButton(withTitle: "OK")
            alert.addButton(withTitle: "Cancel")
            alert.runModal()
            clearCheckBoxes()
            return
        } else {
            // Find the 2 days of interest
            let idxA = buttonResponse.firstIndex(of: 1)!
            let idxB = buttonResponse.lastIndex(of: 1)!
            
            // Find index value for specific meal
            let idxC = arrayOfSideDays[idxA]!.indexOfSelectedItem
            let idxD = arrayOfSideDays[idxB]!.indexOfSelectedItem
            
            // Swap sides
            arrayOfSideDays[idxA]!.selectItem(at: idxD)
            arrayOfSideDays[idxB]!.selectItem(at: idxC)
        }
        
        // Clear all the checkboxes
        clearCheckBoxes()
    }
    
}

