# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

#Solution1:uisng sliding window technique
#TC=O(n)
def noOfSubarrays(arr,k,threshold):

    window_sum=sum(arr[:k])
    count=0

    if window_sum/float(k) >= threshold:
        count+=1
    
    for i in range(k,len(arr)):

        window_sum=window_sum-arr[i-k]+arr[i]

        if window_sum/float(k) >= threshold:
            count+=1

    return count

arr=[2,2,2,2,5,5,5,8]
k=3
threshold=4
result=noOfSubarrays(arr,k,threshold)
print(result)

#Solution2:uisng sliding window technique with more optimized approach using mathematical logic
#MathematicalLogic:
#we are doing : if window_sum / k >= threshold:
#                   count += 1
#we have: window_sum / k >= threshold
#multiply k on both sides
#we get window_sum >= k * threshold
"""
def noOfSubarrays(arr,k,threshold):

    window_sum=sum(arr[:k])
    count=0

    if window_sum >= k * threshold:
        count+=1
    
    for i in range(k,len(arr)):

        window_sum=window_sum-arr[i-k]+arr[i]

        if window_sum >= k * threshold:
            count+=1

    return count
"""