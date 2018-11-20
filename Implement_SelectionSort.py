# Author : Deepak Kumar Singh
# Date: 20/Nov/2018
# This program implements Sdlection sort on a given list.


# Function to find the smallest element in a given array
def findsmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
    

# Function to sort based on Selection sort Algorithm
def SelectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest)) 
    return newArr
    
print(SelectionSort([5,2,6,1,10]))




