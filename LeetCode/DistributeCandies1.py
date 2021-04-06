from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c=Counter(candyType)
        n1=len(candyType)//2
        
        return min(len(c),n1)
