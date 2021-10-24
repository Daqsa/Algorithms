'''
Search array and return its index of the 
first occurance of value x

arr : type array
x : any
'''
def linearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] is x:
            return i
    return None

if __name__ == "__main__":
    index = linearSearch([1, 2, 4, 3, 5], 5)
    print(index)
