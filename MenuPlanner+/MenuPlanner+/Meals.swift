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
        mains = ["Burgers", "Hot Dogs", "Cat Fish", "Hamburgers", "Pasta", "Pasta", "Veggies", "Salmon", "a", "b", "c", "d"]
        mains = Array(Set(mains))
        mains.sort()
        mains.insert("---", at: 0)
        
        idxMains = (1...mains.count).shuffled()
        
        sides = ["Fries", "Gummy Worms", "Salad", "Beans", "Potatoes", "a", "b", "c", "d"]
        sides = Array(Set(sides))
        sides.sort()
        sides.insert("---", at: 0)
        
        idxSides = (1...sides.count).shuffled()
    }
    
}
