class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0
        for i in range(len(nums)):
            
            if nums[i]!=val:
                #print(i)
                nums[a]=nums[i]
                a+=1
                
        return a
