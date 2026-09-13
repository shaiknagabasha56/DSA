#Find the longets common prefix among the array of strings
def longestCommonPrefix(arr,n):
    prefix=""
    i=0
    while True:
        if i>=len(arr[0]):
            return prefix
        temp=arr[0][i]
        for j in range(n):
            if i>=len(arr[j]) or temp!=arr[j][i]:
                return prefix
        prefix+=temp
        i+=1


arr=["flute","flow","flower"]
n=len(arr)
print(longestCommonPrefix(arr,n))

#Time complexity:O(S)
#beats:100%
