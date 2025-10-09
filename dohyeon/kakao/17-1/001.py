from unittest import result


class Solution:
    def solution(self, n, arr1, arr2):
        arr1_bin = []
        arr2_bin = []
        temp_result = []
        result = []
        
        # 각 배열의 요소를 이진수로 변환하여 저장
        for i in range(n):
            arr1_bin.append(self.to_binary(n, arr1[i]))
            arr2_bin.append(self.to_binary(n, arr2[i]))

        # 두 배열 요소를 비교하여 하나라도 1이라면 1, 아니면 0으로 변환 후 temp_result에 저장
        for i in range(n):
            temp = ''
            for j in range(n):
                if arr1_bin[i][j] == '1' or arr2_bin[i][j] == '1':
                    temp += '1'
                else:
                    temp += '0'
            temp_result.append(temp)

        # result의 각 요소 중 1을 #으로, 0을 ' '로 변환
        for i in range(n):
            temp = ''
            for j in range(n):
                if temp_result[i][j] == '1':
                    temp += '#'
                else:
                    temp += ' '
            result.append(temp)

        return result


    def to_binary(self, n, num):
        """n: 자릿수, num: 10진수 숫자"""
        binary = bin(num)[2:] # bin() 함수는 '0b' 접두사를 붙여서 반환하므로, [2:]로 제거
        return '0' * (n - len(binary)) + binary
    

# examples
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
sol = Solution()
print(sol.solution(n, arr1, arr2))  # ['#####', '# # #', '### #', '#  ##', '#####']