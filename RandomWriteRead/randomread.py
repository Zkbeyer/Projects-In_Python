
#function to read the file 
def read_file(file_name):
    f = None
    numbers = []
    try:
        f = open(file_name, 'r')
        for n in f:
            numbers.append(int(n))
    except Exception as error:
        print(error)
    finally:
        if(f != None):
            f.close
    return numbers

#function to print everything
def print_results(numbers, file_name):
    print("List of random numbers in", file_name)
    for n in numbers:
        print(n)
    print("\nrandom number count:", len(numbers))

def main():
    file_name = "randomnum.txt"
    numbers = read_file(file_name)
    print_results(numbers, file_name)

main()
