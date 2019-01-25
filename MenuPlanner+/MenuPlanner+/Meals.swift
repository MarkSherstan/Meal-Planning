//
//  meals.swift
//  MenuPlanner+
//
//  Created by Mark Sherstan on 2019-01-24.
//  Copyright © 2019 Mark Sherstan. All rights reserved.
//

import Foundation


class Meals{
    
    func getMains() -> Array<String> {
        let mains = ["Burgers", "Hot Dogs", "Cat Fish", "Hamburgers", "Pasta", "Pasta", "Veggies", "Salmon"];
        var uniqueMains = Array(Set(mains))
        uniqueMains.sort()
        uniqueMains.insert("---", at: 0)
        return uniqueMains
    }

    func getSides() -> Array<String> {
        let sides = ["Fries", "Gummy Worms", "Salad", "Beans", "Potatoes"];
        var uniqueSides = Array(Set(sides))
        uniqueSides.sort()
        uniqueSides.insert("---", at: 0)
        return uniqueSides
    }
    
}

