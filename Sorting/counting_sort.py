"""

"""
def countingSort(arr, n, m):
    equal = countKeysEqual(arr, n, m)
    print("equal", equal)
    less = countKeysLess(equal, m)
    print("less", less)
    sortedArr = rearrange(arr, less, n, m)
    return sortedArr
    

"""
Make a new array "equal" such that equal[i] = #i's in arr
"""
def countKeysEqual(arr, n, m):
    equal = [0 for i in range(m)]
    for i in range(n):
        key = arr[i]
        equal[key] += 1
    return equal


"""
Make a new array "less" such that less[i] = #elements in arr less than i
"""
def countKeysLess(equal, m):
    less = [0 for i in range(m)]
    for j in range(1, m):
        less[j] = less[j-1] + equal[j-1]
    return less


"""
Idea: if there are less[j] elements less than j, j goes to j+1th index
"""
def rearrange(arr, less, n, m):
    sortedArray = [0 for i in range(n)]
    for i in range(n):
        key = arr[i]
        index = less[key]
        sortedArray[index] = arr[i]
        less[key] += 1
    return sortedArray



if __name__ == "__main__":
    arr = [1,4,3,0,2,3,2,1,4,0,4,4,2,1]
    upperBound = 5
    sortedArr = countingSort(arr, len(arr), upperBound)
    print(sortedArr)
