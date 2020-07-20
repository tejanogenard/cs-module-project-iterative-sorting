def linear_search(arr, target):
    # 1. Check if value at index = value we are searching for 
        #a. if YES: 
            #Great! Return the index 
        #b. if NO: 
            #if the end of the list is reached, return item not found 
            #else, index++ and repeat
    for i in range(0, len(arr)):
        if arr[i] == target: 
            return i 
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #1. Check if value at index = value we are searching for 
        #a. if YES: 
            #Great! Return the index 
        # if NO: 
            #if this was final index to search, return item not found 
            # else if value at index > target value, eliminate RHS, repeat seatch on LHS 
            # else, eliminate LHS, repeat search on RHS 

    low = 0 
    high = len(arr) - 1
    
    while low <= high:
        middle = (low + high) // 2
        if target < arr[middle]:
            high = middle - 1    # eliminate RHS 
        elif target > arr[middle]: 
            low = middle + 1     # eliminate LHS 
        else: 
            return middle 
    return -1  # not found
