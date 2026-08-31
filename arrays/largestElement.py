#Find the largest element in the array:

#Approach-1:using array's index value and comparison
"""
def largestElement(arr):
    largest=arr[0]
    for element in arr:
        if element>=largest:
            largest=element
    return largest

array=[10,20,0,80,15]
print(largestElement(array))
"""

#Approach-2:using max() built-in function
"""
def largestElement(arr):
    return max(arr)
array=[10,20,0,80,15]
print(largestElement(array))
"""

#Approach-3:using sort() built-in function
"""
def largestElement(arr):
    arr.sort(reverse=True)
    return arr[0]
array=[10,20,0,80,15]
print(largestElement(array))
"""

#Approach-4:using sorting (here i have used bubble sort algorithm to sort the array)
"""
def largestElement(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]   #swapping elements
    return arr[n-1]

array=[64,34,25,120,22,11,90]
print(f"largest Element = {largestElement(array)}")
"""

#Note:The above approach causes run-time error.
#test cases containing large arrays (e.g., 10^5 elements), this solution performs billions of operations, causing the system to kill the execution