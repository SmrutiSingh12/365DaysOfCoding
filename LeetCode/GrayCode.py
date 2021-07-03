class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[]
        for i in range(2**n):
            i=i^i//2
            res.append(i)
            
        return res   
 '''
 ^:Xor 
 given n=3:
 2^3=8
 
 0^0=0
 1^0=01^00=01=1
 2^1=10^01=11=3
 3^1=11^01=10=2
 4^2=100^010=110=6
 5^2=101^010=111=7
 6^3=110^011=101=5
 7^3=111^011=100=4
 
 
 [0,1,3,2,6,7,5,4]
 '''
 
