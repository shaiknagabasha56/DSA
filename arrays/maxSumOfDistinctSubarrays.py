#Leetcode:2461 (Max sum of distinct subarrys with length k)
#you are given integer array nums and an integer k. find the maximum subarray sum
#of all the subarrays of nums that meet the following conditions
#the length of the subarray is k and all elements of subarray are distinct
#return the max subarray sum of all the subarrays that meet the conditions. if no subarray meets the condition return 0



#Approach:Fixed Sliding Window
def myfun(arr,k):
    freq={}
    window_sum = sum(arr[:k])
    max_sum = 0

    for i in arr[:k]:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    if len(freq) == k:
        max_sum = window_sum
    
    for i in range(k,len(arr)):
        if arr[i-k] in freq:
            freq[arr[i-k]] -= 1
            if freq[arr[i-k]] == 0:
                del freq[arr[i-k]]
                
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
        
        window_sum = window_sum - arr[i-k] + arr[i]

        
        if len(freq) == k:
            max_sum = max(window_sum,max_sum)
    return max_sum

arr=[9,9,9,1,2,3]
k=3
result=myfun(arr,k)
print(result)
