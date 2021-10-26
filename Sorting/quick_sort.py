"""
Given: arr (array), p (starting index), r (ending index)
Sort arr in non-descending order
"""
def quickSort(arr, p, r):
    if p >= r:
        return None
    q = partition(arr, p, r)
    quickSort(arr, p, q-1)
    quickSort(arr, q+1, r)


"""
Given: arr (array), p (starting index), r (ending index)
Select a pivot, then have all elements left of the pivot be less than or eq to pivot
and all elements right of the pivot be greater than pivot
Any number in array is in Left, Right, Unchecked, or Pivot in that order.

In this version of quicksort, the pivot is the rightmost element of subarray
"""
def partition(arr, p, r):
    q = p
    for u in range(p, r):
        # if arr[u] > arr[r], arr[u] can be in the right place by incrementing u
        # since the Right numbers are immediately left to Unchecked numbers
        if arr[u] <= arr[r]:
            # swap arr[q] and arr[u]
            storage = arr[q]
            arr[q] = arr[u]
            arr[u] = storage
            # current arr[q] is in right place. 
            # so prepare to swap arr[q+1]
            q += 1
    # swap arr[q] and arr[r]
    storage = arr[q] 
    arr[q] = arr[r]
    arr[r] = storage
    return q

if __name__ == "__main__":
    arr = [3,2,6,4,3,8,9,2]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
