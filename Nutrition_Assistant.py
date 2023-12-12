import random
#import re

fruit = ["bananas", "apples", "blueberries", "pineapple", "cantelope", "mango",
         "strawberries", "peaches", "avocado", "dates"]
greens = ["asparagus","brussel sprouts","cauliflower","broccoli",
          "arugula","spinach","butternut squash","collard greens"]
moreveg = ["eggplants","tomatoes","carrots","bell peppers","jalapenos","corn","mushrooms"]
fragrants = ["yellow onions","red onions","garlic"]
acidic = ["lemons","limes"]
herbs = ["rosemary","cilantro","parsley","thyme"]
ferment = ["pickles","greek yogurt","sauerkraut","kimchi","kefir"]
potato = ["sweet potatoes","russet potatoes","baby potatoes"]
rices = ["white rice","brown rice","quinoa","wild rice"]
pastas = ["penne","linguine","rigatoni","gnocchi","tagliatelle","papardelle"]
bread = ["italian bread","sourdough bread","sprouted bread","rye bread","challah bread","naan bread","pita bread","almond tortilla","keto bread"]
cerealz = ["healthier cereal","granola","oats","sugary cereal"]
beans = ["chickpeas","black beans","pinto beans","white beans"]
nuts = ["walnuts","almonds","cashews","brazil nuts"]
tastydipz = ["peanut butter","almond butter","hummus","guacamole"]
sauces = ["salsa","BBQ","ketchup","soy","marinara","mustard","sriracha"]
butterz = ["salted butter","unsalted butter","ghee","coconut oil"]
milks = ["almond milk","low-fat milk","whole milk","coconut milk"]
cheeses = ["cheddar cheese","colby jack cheese","cottage cheese","feta cheese","parmesean cheese",
          "goat cheese"]
seafoods = ["wild salmon","wild cod","wild shrimp","wild scallops","crab"]
poultry = ["eggs","chicken breast","chicken thighs"]
redmeat = ["ground beef","ground lamb","skirt steak","lamb shoulder","sirloin steak"]
additionalvegan = ["tofu","falafel","pumpkin seeds","coconut yogurt"]
additionalsnackz = ["protein bars","granola bars","corn chips","trail mix","popcorn"]

def calorieCalculation(gender,age,weight,height,active,fit):
    if gender == "M" or "Male":
        BMR = 66 + (6.2 * int(weight)) + (12.7 * int(height)) - (6.76 * int(age))
    elif gender == "F" or "Female":
        BMR = 655.1 + (4.35 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age))
    calories = 0
    if active[0] == "s":
        calories = BMR * 1.2
    elif active[0] == "m":
        calories = BMR * 1.375
    elif active[0] == "a":
        calories = BMR * 1.55
    elif active[0] == "v":
        calories = BMR * 1.725
    newcalories = 0
    if fit[0:2] == "lo":
        newcalories = calories * .80
    elif fit [0:2] == "ga":
        newcalories = calories * 1.2
    else:
        newcalories = calories
    return newcalories

def store_identifier(spend):
    store = ""
    if spend < 60:
        store = print("You should shop at Aldi or Walmart")
    elif 60 <= spend <= 80:
        store = print("You should shop at Aldi or Trader Joes")
    elif 81 <= spend <= 110:
        store = print("You should shop at Wegmans or Sprouts")
    elif 110 <= spend <= 150:
        store = print("You should at Whole Foods or MOM's Organic Market")
    else:
        store = print("Go to Costco or Sam's Club. You've got a big family to take care of.")
    return store


def fourEveryone():
    fruitz = random.sample(fruit, 2)
    greenz = random.sample(greens, 3)
    vegge = random.sample(moreveg, 1)
    frag = random.sample(fragrants, 2)
    acids = random.sample(acidic, 1)
    herbals = random.sample(herbs, 1)
    potaterz = random.sample(potato, 1)
    beanz = random.sample(beans, 1)
    print("Based on your preferences, this is what you should look for:")
    print("For Fruit, get", fruitz)
    print("For Veggies, get", greenz, vegge, frag, acids, "and", herbals)
    print("For additional fibers, get", potaterz, "and", beanz)
    print("     ")
    print("Lets continue!!!")
    print("        ")
def fourMost():
    rice = random.sample(rices, 1)
    cereal = random.sample(cerealz, 1)
    sauce = random.sample(sauces, 1)
    milk = random.sample(milks, 1)
    return rice, cereal, sauce, milk
def restrictionz(allergy):
    allergy = allergy.lower()
    if allergy[0] == "d" or allergy[0] == "s":
        return ("You should also get", milks[0], "and", butterz[3])
    elif allergy[0] == "t":
        return ("You should also get", tastydipz[2])
    elif allergy[0] == "g":
        return ("You should also get", bread[7], "and", bread[8])
    elif allergy[0] == "f":
        return ("You should also get", additionalvegan[1])
    else:
        dips = random.sample(tastydipz, 1)
        nutz = random.sample(nuts, 1)
        snackz = random.sample(additionalsnackz, 1)
        return ("You should also get", dips, snackz, "and", nutz)

def dietaryIncome_Restrictionz(diet_Ques):
    diet_Ques = diet_Ques.lower()
    rando = fourMost()
    breads = random.sample(bread, 1)
    butter = random.sample(butterz, 1)
    poult = random.sample(poultry, 1)
    pasta = random.sample(pastas, 1)
    milk = random.sample(milks, 1)
    if diet_Ques[0:4] == "vege":
        return ("Unless allergic, you should consider:", rando, poultry[0], butter, pasta)
    elif diet_Ques[0] == "p" or diet_Ques[0] == "h":
        return ("Unless allergic, you should consider:", rando, breads, butter, pasta, poultry[0], seafoods[0])
    elif diet_Ques[0:4] == "vega" or diet_Ques[0:4] == "veeg":
        return (
        "Unless allergic, you should consider:", ferment[-2], pasta, cerealz[2], breads, sauces[0], butterz[-1], milks[0])
    elif diet_Ques[0:2] == "ke":
        return ("Unless allergic,you should consider:", rices[-2], bread[-2], bread[-1], butter, sauces[0], poult, milk)
    elif diet_Ques[0:2] == "ko":
        return ("Unless allergic, you should consider:", rando, bread[5], butter, poult, pasta)
    else:
        return ("Unless allergic, you should consider:", rando, breads, butter, poult, pasta)

def dietarySpend_Restrictions(allergy, diet_Ques, spend):
    bigcheeseperson = random.sample(cheeses, 2)
    smallcheeseperson = random.sample(cheeses, 1)
    bigvegan = random.sample(additionalvegan, 2)
    bigbean = random.sample(beans, 1)
    bigaddition = random.sample(ferment, 1)
    bigred = random.sample(redmeat, 2)
    bigsea = random.sample(seafoods, 1)
    if spend <= 60 or 61 <= spend <= 80:
        if diet_Ques[0:4] == "vega" or diet_Ques[0:4] == "veeg" or allergy[0] == "d":
            return ("Based on your willingness to spend, you should consider", bigvegan)
        elif diet_Ques[0] == "p" or diet_Ques[0] == "h" or diet_Ques[0] == "v":
            return ("Based on your willingness to spend, you should consider", smallcheeseperson, bigaddition, bigbean)
        else:
            return ("Based on your willingness to spend, you should consider", smallcheeseperson, bigaddition, "and",
                    redmeat[0])
    elif 81 <= spend <= 110:
        if diet_Ques[0:4] == "vega" or diet_Ques[0:4] == "veeg" or allergy[0] == "d":
            return ("Based on your willingness to spend, you should consider", bigvegan, bigbean)
        elif diet_Ques[0] == "p" or diet_Ques[0] == "h" or diet_Ques[0] == "v":
            return ("Based on your willingness to spend, you should consider", bigcheeseperson, bigaddition)
        else:
            return ("Based on your willingness to spend, you should consider", bigred, bigaddition, seafoods[0])
    elif 111 <= spend <= 150:
        if diet_Ques[0:4] == "vega" or diet_Ques[0:4] == "veeg" or allergy[0] == "d":
            return ("Based on your willingness to spend, you should consider", bigvegan, bigbean)
        elif diet_Ques[0] == "p" or diet_Ques[0] == "h" or diet_Ques[0] == "v":
            return ("Based on your willingness to spend, you should consider", bigcheeseperson, bigaddition)
        else:
            return (
            "Based on your willingness to spend, you should consider", bigcheeseperson, bigaddition, bigred, bigsea)
    else:
        if diet_Ques[0:4] == "vega" or diet_Ques[0:4] == "veeg" or allergy[0] == "d":
            return ("Based on your willingness to spend, you should consider", bigvegan, bigbean)
        elif diet_Ques[0] == "p" or diet_Ques[0] == "h" or diet_Ques[0] == "v":
            return ("Based on your willingness to spend, you should consider", bigcheeseperson, bigaddition)
        else:
            return ("Based on your willingness to spend, you should consider", bigcheeseperson, bigaddition, bigred, bigsea)
def mainLoop():
    while True:
        try:
            age = int(input("Enter your age here:"))
            gender = str(input("Enter your gender here(M/F):"))
            weight = int(input("Enter your weight here (lbs):"))
            height = int(input("Enter your height here (inches):"))
            active = str(input("How active are you? (sedentary,moderate,active,very active):"))
            fit = str(input("What are your fitness goals? (lose weight, maintain weight, gain weight):"))
            spend = int(input("How much are you willing to spend per week on food?(enter a digit please): "))
            allergy = str(input("Input any allergies here: (N/None, D/Dairy, T/Tree nuts, S/Soy, G/Gluten, F/Fish):"))
            diet_Ques = str(input("Input any dietary restrictions: (N/None, Vege/Vegetarian, P/Pescatarian, Veeg/Vegan, Ke/Keto, H/Halal, Ko/Kosher)"))
        except ValueError:
            print("Oops, you must've entered the wrong value. Let's retry!!")
            return mainLoop()

        if (calorieCalculation(gender, age, weight, height, active,fit)):
            converted_Cal = (calorieCalculation(gender, age, weight, height, active,fit))
            print("         ")
            print("Starting Here:")
            print("         ")
            print("You should consume", int(converted_Cal), "calories per day")
            print("        ")
        if (store_identifier(spend)):
            storez = (store_identifier(spend))
            print(storez)
        print("       ")
        print("       ")
        if (fourEveryone()):
            hey = (fourEveryone())
            print(hey)
        if (restrictionz(allergy)):
            hay = restrictionz(allergy)
            print(hay)
        if (dietaryIncome_Restrictionz(diet_Ques)):
            hiy = (dietaryIncome_Restrictionz(diet_Ques))
            print(hiy)
        if (dietarySpend_Restrictions(allergy,diet_Ques,spend)):
            hoy = (dietarySpend_Restrictions(allergy,diet_Ques,spend))
            print(hoy)
        print("                               ")
        print("Now you're prepared to achieve quality nutrition for a quality price. ")
        print("Now, it's up to you to grab some of these items and achieve your goals!!")
        print("                                           ")
        rerun = input("Do you want to rerun this (Yes/No):")
        rerun = rerun.lower()
        if rerun == "no" or rerun == "n":
            break
        else:
            return mainLoop()

mainLoop()
