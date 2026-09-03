#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

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