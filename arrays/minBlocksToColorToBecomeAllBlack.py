#Leetcode 2379: Minimum Recolors to Get K Consecutive Black Blocks
#You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' (representing a white block) or 'B' (representing a black block). You are also given an integer k, which is the desired number of consecutive black blocks
#Return the minimum number of recolors needed such that there is at least one occurrence of k consecutive black blocks in blocks.
#In one operation, you can recolor a white block such that it becomes a black block.
def minBlocks(s,k):
    white_count=0
    for ch in s[:k]:
        if ch=='W':
            white_count+=1
    min_count=white_count

    for i in range(k,len(s)):
        if s[i-k] == 'W':
            white_count-=1
        if s[i] == 'W':
            white_count+=1
        min_count=min(min_count,white_count)
    return min_count

s="WBBWWBBWBW"
k=7
result=minBlocks(s,k)
print(result)