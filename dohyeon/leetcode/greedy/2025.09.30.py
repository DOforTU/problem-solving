from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        return self.bagOfTokensScore_sort(tokens, power)
        # return self.bagOfTokensScore_without_sort(tokens, power)
        
    def bagOfTokensScore_without_sort(self, tokens: List[int], power: int) -> int:
        score = 0
        while tokens:
            if len(tokens)==1 and tokens[0] > power:
                return score
            elif len(tokens)==1 and tokens[0] <= power:
                return score + 1 

            if score < 0:
                return score + 1
            
            if min(tokens) <= power:
                power -= min(tokens)
                score += 1
                tokens.pop(tokens.index(min(tokens)))
                continue

            power += max(tokens)
            score -= 1
            tokens.pop(tokens.index(max(tokens)))
            continue

        return score

            
    def bagOfTokensScore_sort(self, tokens: List[int], power: int) -> int:
        # 1. 토큰 배열을 오름차순으로 정렬. (O(N log N))
        tokens.sort()
        
        # 투 포인터 초기화
        left = 0
        right = len(tokens) - 1
        
        score = 0
        max_score = 0
        
        # 2. 투 포인터를 사용하여 그리디 전략 실행 (O(N))
        while left <= right:
            # Case 1: 점수 획득 (Face-up)
            # 현재 power로 가장 작은 토큰을 구매할 수 있다면 무조건 구매.
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                # 획득할 때마다 max_score를 갱신.
                max_score = max(max_score, score)
                
            # Case 2: power 획득 (Face-down)
            # 점수는 있지만, 현재 power로는 점수를 획득할 수 없고,
            # 게임을 계속하기 위해 점수를 팔아 power를 올려야 할 때 (단, 토큰이 1개 남은 경우는 제외)
            elif score >= 1 and left < right:
                # power를 최대로 올리기 위해 가장 큰 토큰을 사용.
                power += tokens[right]
                score -= 1
                right -= 1
                
            # Case 3: 게임 종료 조건
            # power도 부족하고, 점수도 없거나(score < 1), 
            # 토큰이 1개만 남아있어 power를 올려도 점수를 획득할 수 없는 경우 (left == right)
            else:
                break
                
        return max_score