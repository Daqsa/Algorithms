"""
Given: arr (array)
Return: none, sorts the arr in non-descending order

Idea: Take the next element and put it in the right place of the sorted array

for i in range(1, len(arr)):
    set j = i - 1
    set key = arr[i], the element that we'll insert

    while j > 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = key
    
O(n^2) running time, but O(n) if the array is almost sorted
"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
    
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    arr = [5,2,3,4,1]
    insertionSort(arr)
    print(arr)
