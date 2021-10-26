"""
Given: arr (array)
Return: sort the array in non-descending order

Idea: the smallest element comes first

While i < len(arr)
Traverse through the array. 
Find smallest element in arr[i+1..n]
Swap positions with the first element. 
increase i 

O(n^2) but reasonable choice when swapping elements incurs large costs
since swapping occurs only O(n) times
"""
def selection_sort(arr):
    i = 0
    n = len(arr)
    while i < n:
        smallest = arr[i]
        smallestIndex = i
        for j in range(i + 1, n):
            if arr[j] < smallest:
                smallest = arr[j]
                smallestIndex = j
        copy = arr[i] 
        arr[i] = smallest
        arr[smallestIndex] = copy
        i += 1


if __name__ == "__main__":
    arr = [5,4,3,1,2]
    selection_sort(arr)
    print(arr)
