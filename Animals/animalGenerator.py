import Animal

def get_animal():
    animal_type = input("What type of animal would you like to create? ");
    name = input("What is the animal's name? ");
    animal = Animal(animal_type, name);
    return animal;

def print_animal(animal):
    print(animal.get_name() + " the " + animal.get_animal_type() + " is " + animal.get_mood() );

def main():

    animal_list = [];
    another = True;
    
    print("Welcome to the animal generator!");
    print("This program creates Animal objects.");
    while(another == True):
        print("");
        animal_type = input("What type of animal would you like to create? ");
        name = input("What is the animal's name? ");
        animal = Animal.Animal(animal_type, name);
        animal_list.append(animal);
        print("");
        t = input("Would you like to add more animals (y/n)? ");
        if t == "n":
            another = False;
    print("");
    print("Animal List:");
    
    for animal in animal_list:
        print_animal(animal);

    return;

main();
    
    
