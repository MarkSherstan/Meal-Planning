import Cocoa


// Give some random meals, ensure they are unique, and shuffle.
var meals = ["Burgers", "Hot Dogs", "Cat Fish", "Beans", "Hamburgers", "Pasta", "Pasta", "Veggies", "Fish"]
var uniqueMeals = Array(Set(meals))
uniqueMeals.shuffle()
uniqueMeals.append("---")


//// Swap the order of the meals - to be used later
//(uniqueMeals[0], uniqueMeals[1]) = (uniqueMeals[1], uniqueMeals[0])
//print(uniqueMeals[0...4])
//uniqueMeals


// Get the ingrediants of the meal in a dictionary
var meals2 = [
    "Burgers": ["Frozen Burgers", "Pickles", "Ketchup", "Mustard", "Lettuce", "Tomato"],
    "Hot Dogs": ["Ground Beef", "Eggs", "Onions", "Worcestershire Sauce", "Bread Crumbs", "Garlic", "Salt & Pepper", "Ketchup", "Mustard", "Pickles", "Cheese", "Tomato"],
    ]

meals2["Burgers"]


// Initialize ingrediants, test and unwrap the dictionary, append to ingrediants, create unique set of ingrediants
var ingredients = [String]()

for ii in 0...6 {
    if let tempIngredients = meals2[meals[ii]]{
        for jj in 0..<tempIngredients.count{
            ingredients.append(tempIngredients[jj])
        }
    }
}

var ingredientsUnique = Array(Set(ingredients))


// Testing class for meals and ingrediants.
class mealz {
    var main: String
    var ing: String

    init(main: String, ing: String) {
        self.main = main
        self.ing = ing
    }

    func simpleDescription() -> String {
        return "the main is \(main) and the ingrediants are \(ing)"
    }
}

let test = mealz(main: "burgers", ing: "pickles" ) //["pickles", "ketchup"]

test.main
test.ing


// Setting order
print(meals)
meals.count

let mealCount = 0..<meals.count
let mealCountShuffled = mealCount.shuffled()
print(mealCountShuffled)
mealCountShuffled[7]

for ii in 0..<7 {
    let idx = mealCountShuffled[ii]
    print(idx)
    //print(meals[idx])
    print(meals[idx])
}


// Testing functions and disctionaries
var previousMeals = [
    "Monday": ["Stir Fry", "Steak", "Pizza"],
    "Tuesday": ["Lausagna", "Sweet Potatoe Chicken Bacon", "BBQ Chicken"],
]


func test10() -> (Array<String>, Array<String>) {
    let mondayData = ["Stir Fry", "Steak", "Pizza"]
    let tuesdayData = ["Lausagna", "Sweet Potatoe Chicken Bacon", "BBQ Chicken"]
    
    return (mondayData, tuesdayData)
}


var outOut = test10()
outOut.0[2]
outOut.1[outOut.1.count-2]




//
print(meals)

var arr = [0, 0, 1, 1, 0, 0, 0]

let idxA = arr.firstIndex(of: 1)
let idxB = arr.lastIndex(of: 1)


(uniqueMeals[0], uniqueMeals[1]) = (uniqueMeals[1], uniqueMeals[0])
print(uniqueMeals[0...4])
uniqueMeals


