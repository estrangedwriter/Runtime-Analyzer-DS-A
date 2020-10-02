import random
from algorithms import quickSort, mergeSort, bubbleSort, selectionSort, insertionSort
import time

def create_random_list(size, max_val):
    
    random_list = []
    for num in range(size):
        random_list.append(random.randint(0,max_val))

    return random_list

def analyze_func(func_name, arr):
    tic = time.time()
    func_name(arr)
    toc = time.time()
    seconds = toc-tic
    print(f"{func_name.__name__.capitalize()} --> Elapsed time: {seconds:.5f}")

def main_script():
    size = int(input("What size list would you like to create?: "))
    maximum = int(input("What range of numbers would you like?: "))
    run_times = int(input("How many times do you want to run?: "))


    for num in range(run_times):
        print(f"\nRun: {num+1}")
        l = create_random_list(size,maximum)
        analyze_func(bubbleSort, l.copy())
        analyze_func(insertionSort, l.copy())
        analyze_func(selectionSort, l.copy())
        analyze_func(mergeSort,l)
        analyze_func(quickSort,l)
        analyze_func(sorted,l)
        print("-" * 40)

main_script()