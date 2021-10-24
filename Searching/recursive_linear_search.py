"""
implement linear search using recursion
find value x in array arr and return index i

if i > n, return None (base case)
if i <= n and A[i] is x, then return i
if i <= n and A[i] is not x, then return recursive_linear_search(arr, i+1, x)
"""

def recursive_linear_search(arr, x, i = 0):
    global rec
    rec += 1 
    if i > len(arr):
        return None
    else:
        if arr[i] is x:
            return i
        else:
            return recursive_linear_search(arr, x, i + 1)


if __name__ == "__main__":
    rec = 0
    index = recursive_linear_search([2,4,5,6,3,9,0,2,4], 9)
    print(index)
    print("#recursions:", rec)
