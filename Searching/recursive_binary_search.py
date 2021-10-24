"""
Given: arr (array), p (int), r (int), x (any) 
Return: index of x in arr, None if x is not in arr

Assume the array is already sorted in non-descending order,
And the initial call had p = 0 and r = len(arr) - 1
1. if p > r, return None
2. set q = floor((p + r) / 2)
3. if arr[q] is x, then return q
4. otherwise if x < arr[q], then call recursiveBinarySearch(arr, p, q - 1, x)
5. otherwise if arr[q] < x, then call recursiveBinarySearch(arr, p + 1, q, x)
"""
def recursiveBinarySearch(arr, p, r, x):
    if p > r:
        return None
    q = (p + r) // 2
    if arr[q] is x:
        return q
    else:
        if x < arr[q]:
            return recursiveBinarySearch(arr, p, q - 1, x)
        else:
            return recursiveBinarySearch(arr, p + 1, q, x)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    index = recursiveBinarySearch(arr, 0, len(arr), 5)
    print(index)
