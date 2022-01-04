"""
------------------------------------------------------------------------
[displays the number of calories the user as consumed]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-26
------------------------------------------------------------------------
"""
fat_grams = int(input("Enter the fat grams consumed: "))
carbohydrate_grams = int(input("Enter the carbohydrate grams consumed: "))

def calorie_calculator (carbohydrate_grams, fat_grams):
    '''
    ------------------------------------------------------------------------------
    Calculates the calories from inputted fat and carbohydrate values
    ------------------------------------------------------------------------------
    Use: calorie_calculator(carbohydrate_grams,fat_grams)
    >Total calories a total of 1700 [Fat calories: 900 and Carb calories: 800]
    ------------------------------------------------------------------------------
    Paramaters:
        carbohydrate_grams - The amount of carbyhydrates eaten in grams (int > 0)
        fat_grams - The amount of fat eaten in grams (int > 0)
    Returns
        The total calories as well as a breakdown of the calories from carbs and fats (int > 0)
    '''
    carbohydrate_calories = carbohydrate_grams * 4
    fat_calories = fat_grams * 9
    total_calories = fat_calories + carbohydrate_calories
    print("Total calories a total of {:.0f} [Fat calories: {:.0f} and Carb calories: {:.0f}]".format(total_calories,fat_calories,carbohydrate_calories))

calorie_calculator(carbohydrate_grams, fat_grams)