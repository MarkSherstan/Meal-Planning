import Cocoa

var meals = ["Hot Dogs", "Cat Fish", "Beans", "Hamburgers", "Pasta", "Pasta", "Veggies", "Fish"]

var uniqueMeals = Array(Set(meals))

uniqueMeals.shuffle()
uniqueMeals.append("---")


(uniqueMeals[0], uniqueMeals[1]) = (uniqueMeals[1], uniqueMeals[0])


uniqueMeals

