
from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res1=0
        
        c=Counter(nums)
        
        v=c.values()
        for i in v:
            if i==2:
                for key, value in c.items():
                    if i== value:
                        res=key
        n=len(nums)    
        
        
        for j in range(1,n+1):
            
            if j not in nums:
                res1=j
                
        
                
        return res,res1
        
