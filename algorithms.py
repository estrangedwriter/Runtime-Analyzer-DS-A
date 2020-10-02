print("Algorithms file loaded")


def quickSort(arr):

    if len(arr) < 2:
        return arr
    
    else:
        pivot = arr[-1]
        smaller, equal, larger = [],[],[]
        for num in arr:
            if num < pivot:
                smaller.append(num)

            elif num == pivot:
                equal.append(num)
                
            else:
                larger.append(num)
    
        return quickSort(smaller) + equal + quickSort(larger)

def merge_sorted(arr1, arr2):
    sorted_arr = []
    i,j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        
        else:
            sorted_arr.append(arr2[j])
            j +=1
 
    if i < len(arr1):
        for i in range(i,len(arr1)):
            sorted_arr.append(arr1[i])

    elif j < len(arr2):
        for j in range(j,len(arr2)):
            sorted_arr.append(arr2[j])

    return sorted_arr

def mergeSort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergeSort(arr[:middle])
        l2 = mergeSort(arr[middle:])
        return merge_sorted(l1,l2)

def bubbleSort(arr):

    swap_happened = True

    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]

def selectionSort(arr):
    
    length = len(arr)
    index = 0
    
    while index < length:
        for index2 in range(index,length):
            if arr[index] > arr[index2]:
                arr[index], arr[index2] = arr[index2], arr[index]
            else:
                pass

        index +=1

def insertionSort(arr):
    key = 1
    
    while key < len(arr):
        for num in range(key, 0, -1):
            if arr[num] < arr[num-1]:
                arr[num], arr[num-1] = arr[num-1], arr[num]
        key = key + 1
