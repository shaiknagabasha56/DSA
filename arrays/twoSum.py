def twoSum(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(n):
            sum=0
            if i!=j:
                sum=nums[i]+nums[j]
                if sum==target:
                    return [i,j]
    if nums==[]:
        return "null"
    
    return "null"

nums=[2,7,11,15]
target=9
print(twoSum(nums,target))

#The above one is not a optimized one, so for optimized one solve using hash table
#re upload in leetcode because i got O(n^2) instead of O(n)