class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        cnt=0
        k=0
        lsum=0
        s=sum(nums)
        while k < len(nums)-1:
            
            
            lsum+=nums[k]
            s-=nums[k]
            
            if lsum >= s:
                cnt+=1
            k+=1
        return(cnt)