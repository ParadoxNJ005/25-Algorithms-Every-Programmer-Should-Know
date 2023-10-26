class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp =""
        ans = ""
        for i in s:
            if i not in temp:
                temp += i
            else:
                ind = temp.index(i)
                ans = temp if len(temp)>len(ans) else ans
                temp = temp[ind + 1:]
                temp += i
        ans = temp if len(temp) > len(ans) else ans        

        return len(ans)         
"""
Intuition
The problem requires finding the length of the longest substring without
repeating characters in a given string. We can approach this by using a 
sliding window technique to keep track of the current substring without 
repeating characters and update the maximum length found so far.

Approach
Initialize two empty strings, temp and ans, to store the current substring and the longest substring found.
Iterate through each character i in the input string s.
If i is not in the temp substring, append it to temp to extend the current substring.
If i is already in temp, it means a repeating character is found.
Find the index of the first occurrence of i in temp.
Update ans with the longer of temp and the previously stored ans.
Adjust temp by removing characters from the beginning up to and including the first occurrence of i and then append i.
After processing all characters in the input string, check one last time to update ans with the longest substring if it ends at the end of the input string.
Return the length of the longest substring found, which is stored in ans.
"""
