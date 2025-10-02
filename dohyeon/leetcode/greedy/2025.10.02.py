from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        result = 0
        satisfaction.sort()

        # 예외처리
        if min(satisfaction) > 0:
            for i in range(len(satisfaction)):
                result += satisfaction[i] * (i+1)
            return result
        elif min(satisfaction) == 0:
            for i in range(1, len(satisfaction)):
                result += satisfaction[i] * (i+1)
            return result
        elif max(satisfaction) <= 0:
            return result
        
        candidated_result = []
        for i in range(len(satisfaction)):
            time = 1
            temp_result =0
            for j in range(i, len(satisfaction)):
                temp_result += satisfaction[j] * time
                time += 1
            candidated_result.append(temp_result)
        return max(candidated_result)