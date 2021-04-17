class Solution:
    def fib(self, n: int) -> int:
        sum=0
        a=0
        b=1
        if n==1:
            return 1
        for i in range(1,n):
           
            sum=a+b
            a=b
            b=sum
            
            
        return sum
        
