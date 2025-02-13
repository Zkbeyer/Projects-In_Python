do_calculation = True

while do_calculation:
    while True:
        try:
            initial_population = float(input("Input the initial population: "))
            if initial_population < 0:
                print("Negative values are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    while True:
        try:
            growth_rate = float(input("Input the growth rate as a percentage (e.g., 4 for 4%): "))
            if growth_rate < 0:
                print("Negative growth rates are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break
                
    while True:
        try:
            years = float(input("Input the number of years: "))
            if years < 0:
                print("Negative values are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid")
        else:
            break


    future_population = initial_population * ((1 + (growth_rate/100))**years)

    print("The future population would be", round(future_population))

    another_calculation = input("Do you want to perform another calculation? (y/n): ")
    if another_calculation != "y":
        do_calculation = False
