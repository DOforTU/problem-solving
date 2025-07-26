from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # answer: 지금까지 찾은 최대 곱을 저장 (초기값은 음의 무한대)
        answer = -1 * float("inf")
        # prefix: 왼쪽에서부터 곱을 누적 (0을 만나면 1로 리셋)
        prefix = 1
        # suffix: 오른쪽에서부터 곱을 누적 (0을 만나면 1로 리셋)
        suffix = 1
        n = len(nums)

        # - 0이 포함된 경우, 곱이 0이 되므로 0을 만날 때마다 곱을 리셋해야 함
        # - 음수의 개수에 따라 최대 곱이 왼쪽/오른쪽에서 나올 수 있으므로
        #   왼쪽(prefix)과 오른쪽(suffix)에서 각각 누적곱을 계산
        # - 각 위치에서 prefix, suffix, answer 중 최대값을 갱신
        for i in range(n):
            if prefix == 0:
                prefix = 1  # 0을 만나면 곱을 리셋 (새로운 부분배열 시작)
            if suffix == 0:
                suffix = 1  # 0을 만나면 곱을 리셋 (오른쪽에서 새로운 부분배열 시작)
            
            prefix *= nums[i]  # 왼쪽부터 누적곱
            suffix *= nums[n - 1 - i]  # 오른쪽부터 누적곱
            answer = max(answer, prefix, suffix)  # 최대값 갱신

        return answer