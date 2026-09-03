#Find the missing number in an array of size n containing numbers from 1 to n with one number missing.
#Approach-1:Using built-in methods:
"""
def findMissingNums(nums):
    n=len(nums)
    actual_sum=sum(nums)
    expected_sum=(n*(n+1))//2
    return (expected_sum-actual_sum)

arr=[9,6,4,2,3,5,7,0,1]
print(findMissingNums(arr))
"""


#Approach-2:Without using built-in methods:
"""
def findMissingNums(nums):
    n=0
    actual_sum=0
    for i in nums:
        n+=1
        actual_sum+=i
    expected_sum=(n*(n+1))//2
    return (expected_sum-actual_sum)

arr=[0,1,2,3,5,6,7,8]
print(findMissingNums(arr))
"""

