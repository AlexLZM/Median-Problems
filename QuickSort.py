import random
def partition(arr, start_index, end_index):
    '''
    re-arrange the array and 
    return the index where values to its left are less than it 
    and the values to its right are greater than or equal to it
    '''
    pivot_index = random.choice(range(start_index, end_index+1))
    arr[pivot_index], arr[end_index] = arr[end_index], arr[pivot_index]
    i = start_index
    for j in range(start_index, end_index):
        if arr[j] < arr[end_index]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end_index] = arr[end_index], arr[i]
    return i

def quickSort(arr, start_index, end_index):
    '''
    Recursively sort the array inplace on range[start_index, end_index]
    '''
    if len(arr) == 1:
        return
    if start_index < end_index:
        pivot_index = partition(arr, start_index, end_index)
        quickSort(arr, start_index, pivot_index-1)
        quickSort(arr, pivot_index+1, end_index)
        
