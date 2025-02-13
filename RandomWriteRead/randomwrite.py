import random

#function to get positive intiger
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Value must be positive. Please try again.")
                continue
        except ValueError:
            print("Invalid input/ Please enter a valid number.")
        else:
            break
    return value

#function to write a specified quantity of random numbers in a specified range
def write_random(file_name, quantity,lower, upper):
    f = open(file_name, "w")
    for n in range(quantity):
        r = random.randint(lower, upper)
        f.write(str(r))
        f.write("\n")
    f.close


def main():
    file_name = "randomnum.txt"


    print("\n --- Random Writer ---")

    #Gather Input
    quantity = get_positive_int("How many random numbers do you want? ")
    lower = get_positive_int("What's the lowest the random number should be? ")
    upper = get_positive_int("Whats the highest the random number should be? ")

    #Write the random numbers
    write_random(file_name, quantity, lower, upper)

    #print success
    print("numbers have been printed to ""randomnum.txt""")

if __name__ == "__main__":
    main()


    
