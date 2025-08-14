# Given two integers a and b, return the sum of the two integers without using the operators + and -.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32비트 마스크
        mask = 0xFFFFFFFF
        
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        # 음수 처리 (32비트에서 최상위 비트가 1이면 음수)
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        
        return a