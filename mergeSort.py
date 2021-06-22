
def mergeSort(arr):
    '''
    return a sorted array
    '''
    # base case 
    if len(arr) == 1:
        return arr
    
    
    mid = len(arr)//2
    
    # divide the array into 2 sub arrays and sort them separately
    L = mergeSort(arr[:mid])
    R = mergeSort(arr[mid:])

    i = j = 0
    temp = []
    # merge the 2 sorted sub arrays
    # append the smaller elemnt between the two pointed values
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            temp.append(L[i])
            i += 1
        else:
            temp.append(R[j])
            j += 1

    if i < len(L): # append remainder of L if any
        temp.extend(L[i:])
    if j < len(R): # append remainder of R if any
        temp.extend(R[j:])
        
    return temp

            
