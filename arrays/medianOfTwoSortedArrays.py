#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

#Approach-1:Using built-in methods:
"""
def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    n = len(nums1)
    if n%2!=0:
        return nums1[n//2]
    else:
        return float(nums1[n//2]+nums1[n//2-1])/2
        

nums1=[1,2]
nums2=[3,4]
print(findMedianSortedArrays(nums1, nums2))
"""

#Approach-2:Without using built-in methods-used only len()
"""
def findMedianSortedArrays(nums1,nums2):
    n1=len(nums1)
    n2=len(nums2)
    nums1[n1:n1+n2]=nums2[:]
    
    for i in range(len(nums1)):
        for j in range(0,len(nums1)-i-1):
            if nums1[j]>nums1[j+1]:
                nums1[j],nums1[j+1] = nums1[j+1],nums1[j]
    
    if len(nums1)%2!=0:
        return nums1[len(nums1)//2]
    else:
        return float(nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2

arr1=[1,2,3]
arr2=[4,6,5]
print(findMedianSortedArrays(arr1,arr2))
"""

