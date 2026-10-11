#Leetcode 1456: Maximum Number of Vowels in a Substring of Given Length
#Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.


#Approach: Fixed Sliding Window Technique
def no_vowels(str,k):

    vowel_count=0
    max_count=0
    for i in str[:k]:
        if i in "aeiou":
            vowel_count+=1
    max_count=vowel_count

    for i in range(k,len(str)):
        if str[i-k] in "aeiou":
            vowel_count-=1
        if str[i] in "aeiou":
            vowel_count+=1
        max_count=max(vowel_count,max_count)
    return max_count

str="abciiidef"
k=3
result=no_vowels(str,k)
print(result)
#Time Complexity=O(n)
#Space Complexity=O(1)

