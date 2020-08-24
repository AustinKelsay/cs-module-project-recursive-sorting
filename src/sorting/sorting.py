# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    left_pointer = 0
    right_pointer = 0

    # while there are elements in either array

    while left_pointer < len(arrA) and right_pointer < len(arrB):
        if arrA[left_pointer] < arrB[right_pointer]:

            merged_arr.append(arrA[left_pointer])
            left_pointer += 1

        else:
            merged_arr.append(arrB[right_pointer])
            right_pointer += 1

    # If the while loop no longer triggers we know that there are left over elements in either the right array or the left array
    merged_arr.extend(arrA[left_pointer:])
    merged_arr.extend(arrB[right_pointer:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # make sure the list is not empty
    if len(arr) <= 1:
        return arr
    pivot = int(len(arr) / 2)
    # The left half will be everything up to the pivot
    left = merge_sort(arr[:pivot])
    # The right half will be everything starting from the pivot
    right = merge_sort(arr[pivot:])

    return merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

