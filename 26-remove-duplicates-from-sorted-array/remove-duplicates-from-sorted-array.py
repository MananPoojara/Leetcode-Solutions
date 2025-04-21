class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset = set(nums)
        k = 0 

        sorted_num = sorted(hashset)
        for num in sorted_num:
            nums[k] = num
            k +=1
        
        return k

        