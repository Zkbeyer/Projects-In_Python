
#function to get filename input
def inputString(prompt):
    f = None
    while True:
        s = str(input(prompt))
        try:
            f = open(s,'r')
        except Exception as error:
            print(error)
        else:
            break
    if f!= None:
        f.close
    return s
            
#get all of the numbers in the file
def getNumbers(file_name):
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

#funciton for sum
def getSum(num_array):
    total = 0;
    for n in num_array:
        total += n
    return total

#function to count how many numbers
def getCount(num_array):
    return len(num_array)

#function for average
def getAverage(num_array):
    return getSum(num_array)/getCount(num_array)

#function to find max
def getMax(num_array):
    maxInt = num_array[0];
    for n in num_array:
        if n > maxInt:
            maxInt = n
    return maxInt

#function for min
def getMin(num_array):
    maxInt = num_array[0];
    for n in num_array:
        if n < maxInt:
            maxInt = n
    return maxInt

#function for range
def getRange(num_array):
    return getMax(num_array) - getMin(num_array)

#function to print information
def print_info(file_name, num_array):
    #I find values first to try to save on runtime
    minInt = getMin(num_array)
    maxInt = getMax(num_array)
    total = getSum(num_array)
    count = getCount(num_array)
    print("File name: ", file_name)
    print("Sum:", total)
    print("Count:", count)
    #even though I have a function for this, it makes no sense to sum the array a second time
    print("Average:", total/count)
    print("Max:", maxInt)
    print("Min:", minInt)
    print("Range:", maxInt-minInt)
        

def main():
    file_name = inputString("What is the file name? ")
    numbers = getNumbers(file_name)
    print_info(file_name,numbers)
    

main()
    
