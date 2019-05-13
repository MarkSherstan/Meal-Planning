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
    var mains: Array<String>
    var idxMains: Array<Int>
    var sides: Array<String>
    var idxSides: Array<Int>
    
    init() {
        mains = [ "a", "b", "c", "d", "e", "f", "g", "h", "i"]
        mains = Array(Set(mains))
        mains.sort()
        mains.insert("---", at: 0)
        
        idxMains = (1...mains.count-1).shuffled()
        
        sides = ["Fries", "Gummy Worms", "Salad", "Beans", "Potatoes", "nachos", "cookies", "pancakes"]
        sides = Array(Set(sides))
        sides.sort()
        sides.insert("---", at: 0)
        
        idxSides = (1...sides.count-1).shuffled()
    }
    
    
    func updateData(filepath: String){
        // Check on the filepath the user provided
        if (filepath.isEmpty == false){
            do {
                // User provided good data, set up the extraction
                let query = try String(contentsOfFile: filepath)
                let regex = try! NSRegularExpression(pattern:"<h2 itemprop=\"name\">(.*?)</h2>", options: [])
                var results = [String]()
                
                // Extract the meal names
                regex.enumerateMatches(in: query, options: [], range: NSMakeRange(0, query.utf16.count)) { result, flags, stop in
                    if let r = result?.range(at: 1), let range = Range(r, in: query) {
                        results.append(String(query[range]))
                    }
                }
                
                // Update the class
                mains = results
              
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
            // File not found!
            let alert = NSAlert()
            alert.messageText = "File Not Found"
            alert.alertStyle = .warning
            alert.addButton(withTitle: "OK")
            alert.addButton(withTitle: "Cancel")
            alert.runModal()
        }
    }

}
