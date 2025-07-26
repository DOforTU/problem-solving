from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_nums = set(nums)
        
        if len(unique_nums) == len(nums):
            return False
        
        return True