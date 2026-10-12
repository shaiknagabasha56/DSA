#Leetcode:1423. Maximum Points You Can Obtain from Cards
#There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

#Approah: Fixed Sliding Window
def maxPoints(arr,k):
    total_sum=sum(arr)
    t=len(arr)-k
    if t==0:
        return total_sum
    window_sum=sum(arr[:t])
    min_sum=window_sum

    for i in range(t,len(arr)):
        window_sum = window_sum - arr[i-t] + arr[i]
        min_sum = min( window_sum,min_sum)

    return total_sum - min_sum

arr = [9,7,7,9,7,7,9]
k = 7
result = maxPoints(arr,k)
print(result)