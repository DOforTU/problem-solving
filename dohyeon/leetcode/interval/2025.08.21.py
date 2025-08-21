# https://leetcode.com/problems/insert-interval/

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        is_merged = False
        
        # intervals를 순차적으로 탐색:
        # 1. interval의 끝 점이 newInterval의 시작점보다 작다면 result에 저장
        # 2. interval의 시작 점이 newInterval의 끝점보다 작거나 같다면 겹침.
        # 이때 두 충돌 범위에서 최솟값이 시작점, 최댓값이 끝 점이됨. 이 값을 newInterval로 갱신
        # 3. 겹치는게 없다면, result에 newInterval를 추가하고, 나머지 간격 추가.
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                if not is_merged:
                    result.append(newInterval)
                    is_merged = True
                result.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        if not is_merged:
            result.append(newInterval)
            
        return result

    from typing import List

class BetterSolution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. newInterval보다 완전히 앞에 있는 간격들 추가
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # 2. 겹치는 간격들을 병합
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 병합이 끝난 newInterval을 결과에 추가
        result.append(newInterval)
        
        # 3. newInterval보다 완전히 뒤에 있는 간격들 추가
        while i < n:
            result.append(intervals[i])
            i += 1
            
        return result