#Find the second largest element in the array without using sorting:-

#Approach - 1:
"""
def secondLargestElement(arr):
    lar1=arr[0]
    lar2=arr[0]
    for i in arr:
        if i>lar1:
            lar1=i
    for j in arr:
        if j>lar2 and j!=lar1:
            lar2=j
    return lar2
l=[7,2,5,9,0]
print(f"Second Largest Element = {secondLargestElement(l)}")
"""


#Approach - 2:
"""
def secondLargestElement(arr):
    arr.remove(max(arr))
    return max(arr)
l=[7,21,50,9,10]
print(f"Second Largest Element = {secondLargestElement(l)}")
"""

#Approach - 3:
#Finding second largest element in a given array.
"""
arr = [700, 21, 500, 9, 100]
max_ele=float("-inf")
second_max_ele=float("-inf")
for number in arr:
    if number > max_ele:
        second_max_ele=max_ele
        max_ele = number 
    elif number > second_max_ele and number != max_ele:
        second_max_ele=number
print (second_max_ele)
"""