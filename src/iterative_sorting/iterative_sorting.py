# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # iterate through the array (represents the sorted-unsorted boundary 
    # moving across the array)
    for i in range(len(arr)):  # O(n)
        # index of the boundary, as well as the index we're going to 
        # swap the smallest element with 
        boundary = i
        smallest_value = arr[boundary]
        smallest_index = boundary
        # finding the smallest element 
        # in the "unsorted" portion of the array 
        for unsorted_index in range(boundary, len(arr)):  # O(n)
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # `smallest_index` is the index of the smallest element in the unsorted portion 
        # once that's found, swap it with the element on the right edge 
        # of the sorted-unsorted boundary 
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
# Compare the first and second item of a collection. If the first item is bigger than the second item, swap the items.
# Move to the next item. Now, we will compare the second item with the third item. If the second item is bigger than the third, swap the items.
# Do this for every item until the end of the list.
# Repeat steps 1-3 (decrementing “the end of the list” by 1 each time).

    indexing_length = len(arr) - 1  #SCan not apply comparision starting with last item of list (No item to right)
    sorted = False                  #Create variable of sorted and set it equal to false

    while not sorted:               #Repeat until sorted = True
        sorted = True               #Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length):            # For every value in the list
            if arr[i] > arr[i+1]:                      # if value in list is greater than value directly to the right of it,
                sorted = False                         # These values are unsorted
                arr[i], arr[i+1] = arr[i+1], arr[i]    # Switch these values
    return arr                                         # Return our list "unsorted_list" which is not sorted.

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
