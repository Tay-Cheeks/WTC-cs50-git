#prompt the user for a fruit and deliver an output of that fruits caloric level
#dictionary of fruits and their caloric levels
#for loop to iterate through the dictionary
#lower the input for case insensitivity
#user inputs the fruit as per FDA poster(strawberries instead of strawberry)
#therefore, the fruit names in the dictionary should be pluralized
#ignore fruit not in the dictionary, so continue the loop

#def a function that'll access a dict of fruits and their caloric levels
def fruit_calories():
    #dict of fruits and their caloric levels
    fruit = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honey dew melon" : 60,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

        #prompt the user for a fruit
    fruit_input = input("Enter a fruit name: ").lower()

        #check if the input is in the dict
    if fruit_input in fruit:
        print(f"Calories: {fruit[fruit_input]}") #acess the value by indexing into to dict key
    #no else,  so we ignore the fruit not in the dict and do nothing

fruit_calories()

