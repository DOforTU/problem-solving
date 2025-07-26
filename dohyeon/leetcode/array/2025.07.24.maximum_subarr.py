from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        answer = -float("inf")

        for i in nums:
            total += i
            if total > answer:
                answer = total
            if total < 0:
                total = 0

        return answer