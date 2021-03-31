class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        
        if x<0:
            
            return False
            
        else:
            x1=x
            while x1>=1:
                n=int(x1%10)
                rev=rev*10+n
                x1=x1/10
            
            if rev==x:
                
                return True
            
            else:
                
                return False
        
