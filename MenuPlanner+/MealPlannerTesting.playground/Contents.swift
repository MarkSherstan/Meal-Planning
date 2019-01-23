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

