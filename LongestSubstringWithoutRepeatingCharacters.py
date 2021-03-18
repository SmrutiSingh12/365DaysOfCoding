from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        result = 0
        lenS = len(s)
        for i in range(lenS):
            count = 0
            for j in range(i, lenS):
                if s[j] not in s[i:j]:
                    count += 1
                else:
                    break
 
            if count > result:
                result = count

        return result
      
      #link:https://leetcode.com/problems/longest-substring-without-repeating-characters/
