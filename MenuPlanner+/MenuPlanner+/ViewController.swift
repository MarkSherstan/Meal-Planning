//
//  ViewController.swift
//  MenuPlanner+
//
//  Created by Mark Sherstan on 2019-01-21.
//  Copyright © 2019 Mark Sherstan. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    
    // Load in Meals class
    var meals = Meals()
    
    // Make global counter
//    var mealCounter = 7
//    var sideCounter = 7
    
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
    
    @IBOutlet weak var mondayMealPast1: NSTextField!
    @IBOutlet weak var mondayMealPast2: NSTextField!
    @IBOutlet weak var mondayMealPast3: NSTextField!
    
    //
//    var arrayOfMealDays = [NSPopUpButton]()
    
    
    // Do any additional setup after loading the view
    override func viewDidLoad() {
        super.viewDidLoad()

        // Get mains and sides
        let mains = meals.getMains()
        let sides = meals.getSides()
        
        // Randomize the order of the meals and sides
        let mainsCount = 1...mains.count
        let idxMains = mainsCount.shuffled()
        let sidesCount = 1...sides.count
        let idxSides = sidesCount.shuffled()
        
        //
//        arrayOfMealDays = [mondayMeal, tuesdayMeal, wednesdayMeal, thursdayMeal, fridayMeal, saturdayMeal, sundayMeal]
        
        // Populate the previous meals
        setUpPreviousMeals()
        
        // Populate the pop up windows
        setUpPopUpWindows(mains: mains, sides: sides, idxMains: idxMains, idxSides: idxSides)
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
    
    
    
    private func setUpPreviousMeals() {
        let previousMeals = meals.getPreviousMeals()
        
        mondayMealPast1.stringValue = previousMeals.0[previousMeals.0.count - 1]
        mondayMealPast2.stringValue = previousMeals.0[previousMeals.0.count - 2]
        mondayMealPast3.stringValue = previousMeals.0[previousMeals.0.count - 3]
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
    
    ////////////////////////////////////////////////////////////////////////////////////////
    // Buttons
    ////////////////////////////////////////////////////////////////////////////////////////
    
    @IBAction func randomizeMealsButton(_ sender: Any) {
//        print("Hello World")
//        let buttonResponse = [mondayCheckBox.state.rawValue, tuesdayCheckBox.state.rawValue, wednesdayCheckBox.state.rawValue,
//                              thursdayCheckBox.state.rawValue, fridayCheckBox.state.rawValue, saturdayCheckBox.state.rawValue,
//                              sundayCheckBox.state.rawValue]
//
//        var ii = 0
//        for mains in arrayOfMealDays {
//            if (buttonResponse[ii] == 1){
////                print(idxMains)
//                print(mealCounter)
////                mains.selectItem(at: idxMains[mealCounter])
//
//                mealCounter += 1
//            }
//            ii += 1
//        }
    }
    
    
    @IBAction func swapMealsButton(_ sender: Any) {
        let buttonResponse = [mondayCheckBox.state.rawValue, tuesdayCheckBox.state.rawValue, wednesdayCheckBox.state.rawValue,
                              thursdayCheckBox.state.rawValue, fridayCheckBox.state.rawValue, saturdayCheckBox.state.rawValue,
                              sundayCheckBox.state.rawValue]
        
//        let currentMains = [mondayMeal.titleOfSelectedItem]

        if (buttonResponse.reduce(0, +) != 2 ) {
            // Display error if not exactly 2 measls are selected
            let alert = NSAlert()
            alert.messageText = "Select Exactly 2 Meals to Swap"
            alert.alertStyle = .warning
            alert.addButton(withTitle: "OK")
            alert.addButton(withTitle: "Cancel")
            alert.runModal()
            return
        } else {
            
//            let idxA = buttonResponse.firstIndex(of: 1)
//            let idxB = buttonResponse.lastIndex(of: 1)
        }

        // Clear all the checkboxes
        clearCheckBoxes()
    }
    
    
    @IBAction func randomizeSidesButton(_ sender: Any) {
    }
    
    
    @IBAction func swapSidesButton(_ sender: Any) {
    }
    
    
}

