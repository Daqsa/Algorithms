"""
Given: arr (array), p (starting index), r (ending index)
Result: sorts arrin non-descending order

Big idea: divide and conquer, recursion
"""
def mergeSort(arr, p, r):
    if p >= r: # arr is already sorted trivially since it only has at most 1 element
        return arr
    q = (p + r) // 2
    mergeSort(arr, p, q)
    mergeSort(arr, q + 1, r)
    merge(arr, p, q, r)


def merge(arr, p, q, r):
    arrB = arr[p : q + 1]
    arrC = arr[q + 1 : r + 1]
    arrB.append(float('inf'))
    arrC.append(float('inf'))
    i, j = 0, 0
    for k in range(p, r + 1):
        if arrB[i] <= arrC[j]:
            arr[k] = arrB[i]
            i += 1
        else:
            arr[k] = arrC[j]
            j += 1

if __name__ == "__main__":
    arr = [4,3,5,2,6,17,8,3]
    mergeSort(arr, 0, len(arr) - 1)
    print(arr)
