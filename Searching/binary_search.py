"""
Given: arr (array), x (any)
Return: index of x in arr, None if x is not in arr

Assume the array is already sorted in non-descending order,
1. Set p = 1, r = len(arr)
2. while p <= r, 
    a) set q = floor((p + r) / 2)
    b) if arr[q] is x, then return q
    c) otherwise if x < arr[q], then set r = q - 1
    d) otherwise if arr[q] < x, then set p = q + 1
3. return None

Time Complexity: O(lg(n)), where n = len(arr)
"""
def binarySearch(arr, x):
    p = 1
    r = len(arr)
    while p <= r:
        q = (p + r) // 2
        if arr[q] is x:
            return q
        else:
            if x < arr[q]:
                r = q - 1
            else:
                p = q + 1
    return None

if __name__ == "__main__":
    index = binarySearch([1,2,3,4,5,6,7,8], 5)
    print(index)
