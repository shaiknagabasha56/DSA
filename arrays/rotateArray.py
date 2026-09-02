#Rotate the array based on the k value
#Solution-1:
"""
def rotateArray(nums,k):
    n=len(nums)
    k=k%n
    if k==0 or k==n:
        return nums
    else:
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
        return nums
           
    
array=[1,2,3,4,5,6,7]
k=3
print(rotateArray(array,k))
"""

#Solution-2:
"""
def rotateArray(nums,k):
     # Get the actual number of rotations
       k = k % len(nums)      
       # Get the number of elements to move from the end to the beginning
       r = len(nums) - k
       # Store the elements to move
       new = nums[0:r]
       # Remove the elements from the beginning
       nums[0:r] = []
       # Append the stored elements to the end
       nums.extend(new)
       return nums
"""


#Solution-3:Without builtin functions
def rotateArray(nums,k):
    n=len(nums)
    k=k%n
    if k==0 or k==n:
        return nums
    else:
        #Reverse the entire array:
        temp=n-1
        for i in range(n//2):
            nums[i],nums[temp]=nums[temp],nums[i]
            temp=temp-1
        #Reverse the first k elements:
        temp=k-1
        for i in range(k//2):
            nums[i],nums[temp]=nums[temp],nums[i]
            temp=temp-1
        #Reverse the remaining n-k elements:
        temp=n-1
        for i in range(k,(n+k)//2):
            nums[i],nums[temp]=nums[temp],nums[i]
            temp=temp-1
        return nums

array=[9,0,1,4,6,7,7,2,9,7]
k=4
print(rotateArray(array,k))
