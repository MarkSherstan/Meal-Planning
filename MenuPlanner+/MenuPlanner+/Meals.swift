//
//  meals.swift
//  MenuPlanner+
//
//  Created by Mark Sherstan on 2019-01-24.
//  Copyright © 2019 Mark Sherstan. All rights reserved.
//

import Foundation
import Cocoa

class Meals{
    // Set data types
    var mains: Array<String>
    var idxMains: Array<Int>
    var sides: Array<String>
    var idxSides: Array<Int>
    
    init() {
        // Set all drop downs to nothing until the user loads some data
        mains = [""]
        idxMains = [0, 0, 0, 0, 0, 0, 0]
        sides = [""]
        idxSides = [0, 0, 0, 0, 0, 0, 0]
    }
    
    
    func updateData(filepath: String){
        // Check on the filepath the user provided
        if (filepath.isEmpty == false){
            do {
                // User provided good data, set up the extraction
                let query = try String(contentsOfFile: filepath)
                let food = filterData(delimiter: "<h2 itemprop=\"name\">(.*?)</h2>", query: query)
                let course = filterData(delimiter: "<span itemprop=\"recipeCourse\">(.*?)</span>", query: query)
                
                // Sort sides and mains and then update the class
                sortData(food: food, course: course)
                
            } catch {
                // Contents could not be loaded
                let alert = NSAlert()
                alert.messageText = "Contents Could Not Be Loaded"
                alert.alertStyle = .warning
                alert.addButton(withTitle: "OK")
                alert.addButton(withTitle: "Cancel")
                alert.runModal()
            }
            
        } else {
            // File not found
            let alert = NSAlert()
            alert.messageText = "File Not Found"
            alert.alertStyle = .warning
            alert.addButton(withTitle: "OK")
            alert.addButton(withTitle: "Cancel")
            alert.runModal()
        }
    }
    
    
    func filterData(delimiter: String, query: String) -> Array<String> {
        // Set up regex and allocate results
        let regex = try! NSRegularExpression(pattern: delimiter, options: [])
        var results = [String]()
        
        // Extract the meal names
        regex.enumerateMatches(in: query, options: [], range: NSMakeRange(0, query.utf16.count)) { result, flags, stop in
            if let r = result?.range(at: 1), let range = Range(r, in: query) {
                results.append(String(query[range]))
            }
        }
        
        // Return the results
        return results
    }
    
    
    func sortData(food: Array<String>, course: Array<String>) {
        // Pre allocate the mains and sides
        var MAINS = [String]()
        var SIDES = [String]()
        
        // Sort out the mains and sides
        for (a, b) in zip(food, course){
            if b == "Main Dish" {
                MAINS.append(a)
            } else if b == "Side Dish" {
                SIDES.append(a)
            }
        }
        
        // Update the class
        mains = Array(Set(MAINS))
        mains.sort()
        mains.insert("---", at: 0)
        idxMains = (1...mains.count-1).shuffled()
        
        sides = Array(Set(SIDES))
        sides.sort()
        sides.insert("---", at: 0)
        idxSides = (1...sides.count-1).shuffled()
    }

}
