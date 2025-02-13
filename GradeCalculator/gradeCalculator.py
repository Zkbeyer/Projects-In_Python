#This program takes user input to fill up a gradebook and allow the user to
#test different grades and weights for their classes

#The user has the ability to calculate thier final grade and continue
#editing their gradebook as much as they like


#gets an int input
def inputInt(prompt):
    while True:
        try:
            n = float(input(prompt))
        except Exception as error:
            print(error)
        else:
            break
    return n

#get string input
def inputString(prompt):
    while True:
        try:
            n = str(input(prompt))
        except Exception as error:
            print(error)
        else:
            break
    return n

#funciton to add a category to the final grade
def addCategory(dictionary):
    category = inputString("Name this category: ")
    if category in dictionary:
        if inputString("would you like to overwrite previous category? (y/n):  ") == "n":
            print("test")
            return
    weight = inputInt("Input the wieght (ex: 20% type 20): ")
    grade = inputInt("Input the grade (ex: 90% type 90): ")
    dictionary[category] = [weight, grade]

#function to delete a category
def deleteCategory( dictionary):
    while True:
        category = inputString("What category are you deleting: ")
        if category in dictionary :
            del dictionary[category]
            return
        else:
            if inputString("Category not found, try something else? (y/n): ") == "n":
                return

#function to edit an existing category
def editCategory(dictionary):
    while True:
        category = inputString("What category are you editing: ")
        if category in dictionary :
            weight = inputInt("Input the wieght (ex: 20% type 20): ")
            grade = inputInt("Input the grade (ex: 90% type 90): ")
            dictionary[category] = [weight, grade]
            return
        else:
            if inputString("Category not found, try something else? (y/n): ") == "n":
                return
#function to make sure weights add up to 100% (-1 means less than 100, -2 means more than 100)
def checkPercent(dictionary):
    total = 0
    for category in dictionary:
        total = total + dictionary[category][0]
    if total < 100:
        return -1
    if total > 100:
        return -2
    else:
        return True

#function to check letter grade
def getLetterGrade(grade):
    if grade < 65:
        return "D-"
    elif grade <= 66:
        return "D"
    elif grade <= 69:
        return "D+"
    elif grade <= 72:
        return "C-"
    elif grade <= 76:
        return "C"
    elif grade <= 79:
        return "C+"
    elif grade <= 82:
        return "B-"
    elif grade <= 86:
        return "B"
    elif grade <= 89:
        return "B+"
    elif grade <= 92:
        return "A-"
    elif grade <= 96:
        return "A"
    else:
        return "A+"


#function to calculate final grade
def calculateGrade(dictionary):
    error = checkPercent(dictionary)
    if error == -1:
        if inputString("Weights dont add up to 100%, are you sure you want to continue? (y/n): ") == "n":
            return
    if error == -2:
        if inputString("Weights add up to more than 100%, are you sure you want to continue? (y/n): ") == "n":
            return
    grade = 0
    for category in dictionary:
        grade = grade + ((dictionary[category][0] / 100) * (dictionary[category][1]))
    letter = getLetterGrade(int(grade))
    print("Your final grade is " + str(round(grade, 2)) + "%")
    print("You would recieve a " + str(letter) + " for this course")

#function to reset the gradebook
def reset(dictionary):
    dictionary.clear()

#function to print the dictionary cleanly
def printGrades(dictionary):
    for category in dictionary:
        print(category + ":")
        print("Weight: " + str(dictionary[category][0]) + "%")
        print("Grade: " + str(dictionary[category][1]) + "%")
        print(" ")

#function to handle input from options
def optionHandler(dictionary):
    while True:
        printOptions()
        select = inputInt("Input Selection: ")
        print(" ")
        if select == 1:
            addCategory(dictionary)
        elif select == 2:
            deleteCategory(dictionary)
        elif select == 3:
            editCategory(dictionary)
        elif select == 4:
            calculateGrade(dictionary)
        elif select == 5:
            printGrades(dictionary)
        elif select == 6:
            reset(dictionary)
        elif select == 7:
            return
        else:
            print("Input not recognized, try agian")


#prints all options
def printOptions():
    print(" ")
    print("1: Add Category")
    print("2: Delete Category")
    print("3: Edit Category")
    print("4: Calculate")
    print("5: Print Categories")
    print("6: Reset Gradebook")
    print("7: Exit")
    print(" ")


def main():
    gradebook = {}
    print("----------GRADE CALCULATOR----------")
    optionHandler(gradebook)
    return


    
    
    

main()
