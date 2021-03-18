class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=""
        if s==s[::-1]:
            return s
        for a in range(n):
            for b in range(n,a,-1):
                
                if len(res)>=b-a:
                    break
                    
                elif (s[a:b]==s[a:b][::-1]):
                    res=s[a:b]
                    
        return res
                
