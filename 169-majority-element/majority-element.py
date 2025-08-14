class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        maj_ele = None

        for num in nums:
            if cnt == 0:
                maj_ele = num
                cnt = 1
            elif maj_ele == num:
                cnt += 1
            else :
                cnt -= 1
        
        return maj_ele

        
        