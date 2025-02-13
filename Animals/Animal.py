import random

class Animal:
    
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type;
        self.__name = name;
        rand = random.randint(1,3);
        match(rand):
            case 1:
                self.__mood = "happy";
            case 2:
                self.__mood = "hungry";
            case 3:
                self.__mood = "sleepy";

    def get_animal_type(self):
        return self.__animal_type;

    def get_name(self):
        return self.__name;

    def get_mood(self):
        return self.__mood;
            
