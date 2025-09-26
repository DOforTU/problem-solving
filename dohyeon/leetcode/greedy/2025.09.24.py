class Solution:
    def longestPalindrome(self, s: str) -> int:
        strings = {}
        count = 0
        for i in s:
            if i in strings:
                strings[i] += 1
            else:
                strings[i] = 1
        
        odd_max_count = 0
        flag = False
        for i in strings:
            if strings[i]%2 == 0:
                count += strings[i]
            else:
                count += strings[i]-1
                flag = True

        return count + int(flag)