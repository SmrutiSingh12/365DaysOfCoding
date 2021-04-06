from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count=0
        
        count=len(candyType)
        
        res=[]
        for i in candyType:
            if i not in res:
                res.append(i)
                
        
        
        r1=len(res)
        r2=int(count/2)
        
        return min(r1,r2)
        
