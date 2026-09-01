#Check if the array is sorted or not:

#Approach - 1:
"""
def checkArraySorted(arr):
    for i in range(len(arr)-1):
        if arr[i]<=arr[i+1]:
            continue
        else:
            return "Not sorted"
    return "sorted"

l=[1,12,30,4,5]
print(f"Is the array sorted? = {checkArraySorted(l)}")
"""


#Approach - 2:
def checkArraySorted(arr):
    if arr==sorted(arr):
        return "sorted"
    else:
        return "Not sorted"
l=[1,12,30,4,5]
print(f"Is the array sorted? = {checkArraySorted(l)}")

print(sorted([1, 2, 30, 4, 5]))