#Leetcode:2134 (min swaps to group all 1's together)
#You are given a binary array nums. You are allowed to swap any two elements of the array. Return the minimum number of swaps required to group all 1's present in the array together


#Approach:Fixed Sliding Window
def minSwaps(nums):
    k = nums.count(1)
    zeros_count = 0

    for i in range(k):
        if nums[i] == 0:
            zeros_count += 1
    min_swaps = zeros_count
    for i in range(k,len(nums)+k-1):
        outgoing = nums[(i-k)%len(nums)]
        incoming = nums[i%len(nums)]
        if outgoing == 0:
            zeros_count -= 1
        if incoming == 0:
            zeros_count += 1
        min_swaps = min(min_swaps,zeros_count)
    return min_swaps

arr=[1,0,1,0,1]
result=minSwaps(arr)
print(result)
            