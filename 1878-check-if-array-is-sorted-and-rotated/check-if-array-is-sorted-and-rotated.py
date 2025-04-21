class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        
        if nums[0] < nums[-1]:
            cnt += 1
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
            
            if cnt > 1:
                return False
        
        return True
        