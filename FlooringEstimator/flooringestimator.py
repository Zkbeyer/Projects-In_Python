do_calculation = True

while do_calculation:
    while True:
        try:
            length = float(input("Input the length of the floor in feet: "))
            if length < 0:
                print("Negative values are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numericle values are valid.")
        else:
            break

    while True:
        try:
            width = float(input("Input the width of the floor in feet: "))
            if width < 0:
                print("Negative values are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numericle values are valid.")
        else:
            break

    while True:
        try:
            box_cost = float(input("Input the cost of tiles per box in $: "))
            if box_cost < 0:
                print("Negative values are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numericle values are valid.")
        else:
            break

    while True:
        try:
            labor_cost_hourly = float(input("Input the Labor cost per hour in $: "))
            if labor_cost_hourly < 0:
                print("Negative values are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numericle values are valid.")
        else:
            break

    square_footage = round(length * width)
    box_count = round(square_footage / 25)
    labor_hours = (square_footage / 50) * 1.5
    tile_cost = box_cost * box_count
    labor_charge = labor_hours * labor_cost_hourly
    total_cost = tile_cost + labor_charge

    print("")
    print(f"For a {square_footage} square foot room, with a box of tiles costing ${box_cost:.2f}, and a labor rate of ${labor_cost_hourly:.2f} per hour:")
    print("")
    print(f"This job will require {box_count} boxes")
    print(f"This job will require {labor_hours:.1f} hours to complete")
    print(f"The tiles will cost ${tile_cost:.2f}")
    print(f"The labor will cost ${labor_charge:.2f}")
    print(f"The total cost of the flooring installation is ${total_cost:.2f}")
    print("")

    again = (input("Would you like to continue? (y/n): "))
    if again != "y":
        do_calculation = False
    
    

