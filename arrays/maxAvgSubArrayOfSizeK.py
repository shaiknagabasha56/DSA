#Leetcode:643. Maximum Average Subarray:
#You are given an integer array nums consisting of n elements, and an integer k.
#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
#I have tried 3 approaches in the last approach i got optimized solution and i have learned sliding window approach
#Im writing this approach-3 first because it has optimized solution 


#Approach3:Sliding Window Approach (Optimized solution)
#TC=O(n)
"""
def maxSubArrayOfsizek(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        max_sum=max(max_sum,window_sum)
    return float(max_sum)/k

arr=[100,200,300,400]
k=2
result=maxSubArrayOfsizek(arr,k)
print(result)
"""

#Approach-1:using nested loops(not optimized solution)
#Tc=O(n*k)pp
"""
def maxSubArrayOfSizek(arr,k):
    n=len(arr)
    max_sum=0
    for i in range(n-(k-1)):
        j=i+k-1
        sum=0
        for l in range(i,j+1):
            sum+=arr[l]
        if sum>=max_sum:
            max_sum=sum
    return float(max_sum)/k

arr=[1,4,2,10,23,3,1,0,20]
k=4
print(maxSubArrayOfSizek(arr,k))
print(sum(arr))
"""


#Approach-2:using slicing technique(not optimized solution)
#TC=O(n*k)
"""
def maxSubArrayOFSizeK(arr,k):
    max_sum=0
    n=len(arr)
    for i in range(n-(k-1)):
        temp=sum(arr[i:(i+k-1)+1])
        if temp>max_sum:
            max_sum=temp
    return max_sum

arr=[2,1,5,1,3,2]
k=3
print(maxSubArrayOFSizeK(arr,k))
"""

#Approach3:Sliding Window Approach (Optimized solution)
#TC=O(n)
"""
def maxSubArrayOfsizek(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum
    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]
        max_sum=max(max_sum,window_sum)
    return float(max_sum)/k

arr=[100,200,300,400]
k=2
result=maxSubArrayOfsizek(arr,k)
print(result)
"""

print(1+12-5-6)