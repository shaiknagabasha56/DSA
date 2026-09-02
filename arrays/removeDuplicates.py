#Remove duplicates from the sorted array(non decrement order):
def removeDuplicates(nums):
        expectedNums=list(set(nums))
        expectedNums.sort()
        k=len(expectedNums)
        return k,expectedNums
l=[1,1,2,2,3,4,4,]
print(f"Length of the array after removing duplicates = {removeDuplicates(l)}")

#not completed.