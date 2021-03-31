class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        y=pow(2,31)
        if x>0:
            
            while x>=1:
                n=int(x%10)
            
                rev=n+rev*10
                x=x/10
            if rev<y-1:
                return rev
            else:
                return 0
        
        
        else:
            rev=0
            x=-(x)
            y=pow(2,31)
            
            while x>=1: 
                n=int(x%10)
            
                rev=n+rev*10
                x=x/10
                
            if rev<y:
            
                return -(rev)
            else:
                return 0
              
              
              
  '''
  https://leetcode.com/problems/reverse-integer/
  '''
        
