from typing import List


# class Solution:
#     # 사용자 정의 비교 함수
#     def compare_nums(self, x, y):
#         """
#         문자열 x와 y를 비교하여 정렬 순서를 결정합니다.
#         x + y > y + x 이면, x가 y보다 앞에 와야 하므로 양수(1) 반환
#         """
#         if x + y > y + x:
#             return -1  # 내림차순 정렬을 위해 x를 앞으로 (-1 반환)
#         elif x + y < y + x:
#             return 1   # y를 앞으로 (1 반환)
#         else:
#             return 0

#     def largestNumber(self, nums: List[int]) -> str:
#         # 1. 모든 숫자를 문자열로 변환
#         str_nums = [str(num) for num in nums]
        
#         # 2. 커스텀 비교 기준을 사용하여 정렬
#         #    - cmp_to_key는 Python 3에서 커스텀 비교 함수를 key로 사용할 수 있게 변환해 줌
#         str_nums.sort(key=cmp_to_key(self.compare_nums))
        
#         # 3. 정렬된 문자열을 합치기
#         result = "".join(str_nums)
        
#         # 4. 예외 처리: 결과가 "000..."일 경우 "0" 반환
#         #    - 리스트가 [0, 0]일 때 결과는 "00"이지만, "0"을 반환해야 함
#         if result[0] == '0':
#             return "0"
        
#         return result

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1. 모든 숫자를 문자열로 변환
        str_nums = [str(num) for num in nums]

        # 2. O(N^2) 버블 정렬을 사용하여 커스텀 정렬 수행 --> sort함수 쓰면 빠름
        n = len(str_nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                # 핵심 비교 로직: str_nums[j]와 str_nums[j+1]을 비교
                # 'str_nums[j] + str_nums[j+1]'이 더 작다면, 순서를 바꿔야 함
                # 작은 수가 뒤로 오도록
                
                if str_nums[j] + str_nums[j+1] < str_nums[j+1] + str_nums[j]:
                    # 자리 교환 (Swap)
                    str_nums[j], str_nums[j+1] = str_nums[j+1], str_nums[j]

        # 3. 정렬된 문자열을 합치기
        result = "".join(str_nums)

        # 4. 예외 처리: 결과가 '000...'일 경우 '0' 반환
        if result and result[0] == '0':
            return "0"
        
        return result