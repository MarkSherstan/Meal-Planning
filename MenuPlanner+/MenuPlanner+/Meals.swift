//
//  meals.swift
//  MenuPlanner+
//
//  Created by Mark Sherstan on 2019-01-24.
//  Copyright © 2019 Mark Sherstan. All rights reserved.
//

import Foundation


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
    
}
