# https://leetcode.com/problems/container-with-most-water/description/
from typing import List

class Solution:
    def _maxArea(self, height: List[int]) -> int:
        """시간초과 발생"""
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                distance = j-i
                max_area = max(max_area, min(height[i], height[j]) * distance)

        return max_area

    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # 현재 너비
            width = right - left
            # 물의 높이는 두 선 중 더 짧은 선에 의해 결정
            current_height = min(height[left], height[right])
            # 현재 넓이 계산
            current_area = width * current_height
            # 최대 넓이 업데이트
            max_area = max(max_area, current_area)

            # 더 큰 넓이를 찾기 위해 포인터 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area