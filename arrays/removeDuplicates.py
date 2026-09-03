#Remove duplicates from the sorted array(non decrement order):
def removeDuplicates(nums):
        i=0
        j=1
        while j<len(nums):
                if nums[i]==nums[j]:
                        j+=1
                else:
                        i+=1
                        nums[i]=nums[j]
                        j+=1
        return nums

nums=[1,1,2,3,3]
print(removeDuplicates(nums))