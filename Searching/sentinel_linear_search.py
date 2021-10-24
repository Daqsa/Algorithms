"""
Search for value x in array arr and return index if found

Perform linear search assuming there is an x in arr.
Change the last element of arr to x, so that there is an x in arr.
Traverse through arr until the current element is x
If we've found an x before the last element, then it works normally
If we've found an x at the last element, we check if the original last element was x
Otherwise, return None
This is an unnecessary optimization (don't have to check if i<=n) but it is one so...

arr: array type
x: any type
"""
def sentinelLinearSearch(arr, x):
    last = arr[-1]
    arr[-1] = x
    i = 0
    while(arr[i] is not x):
        i += 1
    arr[-1] = last
    if i < len(arr) - 1 or arr[-1] is x:
        return i
    else:
        return None


if __name__ == "__main__":
    index = sentinelLinearSearch([1,2,4,3,35,1], 5)
    print(index)
