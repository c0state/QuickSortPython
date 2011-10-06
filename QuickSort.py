import random

def quicksort(array):
    if len(array) < 2:
        return array
    
    # select a random pivot
    pivot = array[random.randint(0, len(array) - 1)]
    array.remove(pivot)
    
    less = []
    greater = []
    
    for elem in array:
        if elem < pivot:
            less.append(elem)
        else:
            greater.append(elem)
    
    return quicksort(less) + [pivot] + quicksort(greater)

if __name__ == "__main__":
    
    array = [ random.randint(0, 100) for i in range(0, 10) ]
    
    print("Initial array is:", array)
    print("Quicksorted array is:", quicksort(array))
