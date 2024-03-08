from colorama import Fore, Style

def bubble_sort(array):
    n = len(array)
    for i in range(n-2):
        for j in range(1, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print_step(array, j, j+1)
                print("After swapping {} and {}: {}".format(array[j], array[j+1], array))
    return array

def read_array_from_file(filename):
    with open(filename, 'r') as file:
        array = [int(num) for num in file.readline().strip().split(',')[1:]] 
    return array

def print_step(array, idx1, idx2):
    for idx, num in enumerate(array):
        if idx == idx1 or idx == idx2:
            print(Fore.GREEN + str(num), end=' ')
        else:
            print(num, end=' ')
    print(Style.RESET_ALL)

filename = "input_array.txt"
array = read_array_from_file(filename)
print("Length of the original array:", len(array))
print("Original array:", array)
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)
print("Length of the sorted array:", len(sorted_array))
