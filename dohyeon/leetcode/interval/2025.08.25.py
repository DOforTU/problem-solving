# https://leetcode.com/problems/merge-intervals/description/

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        # intervals를 start 기준으로 정렬
        intervals.sort(key=lambda x: x[0])

        result = []
        merged = intervals[0]
        merge_finish = False

        for i in range(1, len(intervals)):
            if intervals[i][0] <= merged[1]:
                # merge 해야하는 경우
                merge_finish = False
                merged[1] = max(merged[1], intervals[i][1])
            else:
                # merge 할 필요가 없는 경우
                result.append(merged)
                merged = intervals[i]
            
        result.append(merged)    
        return result