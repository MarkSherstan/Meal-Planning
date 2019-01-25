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
    
    // Monday
    @IBOutlet weak var mondayMeal: NSPopUpButton!
    @IBOutlet weak var mondaySide: NSPopUpButton!
    @IBOutlet weak var mondayMealPast1: NSTextField!
    @IBOutlet weak var mondayMealPast2: NSTextField!
    @IBOutlet weak var mondayMealPast3: NSTextField!
    @IBOutlet weak var mondayCheckBox: NSButton!
    
    // Do any additional setup after loading the view
    override func viewDidLoad() {
        super.viewDidLoad()

        // Get mains and sides
        let mains = meals.getMains()
        let sides = meals.getSides()
        
        // Populate the previous meals
        setUpPreviousMeals()
        
        // Populate the pop up windows
        setUpPopUpWindows(mains: mains, sides: sides)
    }
    
    // Update the view, if already loaded
    override var representedObject: Any? {
        didSet {
        }
    }

    
    ////////////////////////////////////////////////////////////////////////////////////////
    // Private Functions
    ////////////////////////////////////////////////////////////////////////////////////////
    private func setUpPopUpWindows(mains: Array<String>, sides: Array<String>) {
        // Setup the pop up buttons
        mondayMeal.removeAllItems()
        mondayMeal.addItems(withTitles: mains)
        
        let mainsCount = 1...mains.count
        let idxMains = mainsCount.shuffled()
        
        mondayMeal.selectItem(at: idxMains[0])
        
        
        
        mondaySide.removeAllItems()
        mondaySide.addItems(withTitles: sides)
        
        let sidesCount = 1...sides.count
        let idxSides = sidesCount.shuffled()
        
        mondaySide.selectItem(at: idxSides[0])
    }
    
    
    
    private func setUpPreviousMeals() {
        let previousMeals = meals.getPreviousMeals()
        
        mondayMealPast1.stringValue = previousMeals.0[previousMeals.0.count - 1]
        mondayMealPast2.stringValue = previousMeals.0[previousMeals.0.count - 2]
        mondayMealPast3.stringValue = previousMeals.0[previousMeals.0.count - 3]
    }
    
    
    ////////////////////////////////////////////////////////////////////////////////////////
    // Buttons
    ////////////////////////////////////////////////////////////////////////////////////////
    
    @IBAction func randomizeMealsButton(_ sender: Any) {
    
        if mondayCheckBox.state == .on {
            mondayMealPast1.stringValue = "Button On"
        } else {
            mondayMealPast1.stringValue = "Button Off"
        }
        mondayCheckBox.state = .off
    }

    
}

