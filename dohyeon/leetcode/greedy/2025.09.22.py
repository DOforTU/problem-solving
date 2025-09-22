# https://leetcode.com/problems/gas-station/description/?envType=problem-list-v2&envId=vmjsmgog

from typing import List


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         tank = 0
#         start = 0
#         move = 0

#         # 시작 station 탐색
#         for i in range(len(gas)):
#             if gas[i] < cost[i]:
#                 continue
            
#             # 시작 station으로 tank init
#             start = i
#             tank = gas[start]
#             for j in range(len(gas)):
#                 print(tank, '-', cost[start%len(gas)], '+', gas[(start+1)%len(gas)])
#                 tank = tank - cost[start%len(gas)] + gas[(start+1)%len(gas)]

#                 if tank < 0:
#                     break
#                 start += 1
#                 move += 1
                
#                 if move == len(gas)-1 and tank >= cost[start%len(gas)]:
#                     return i

#         return -1
            
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = sum(gas)
        total_cost = sum(cost)

        # 총 gas가 총 cost보다 적으면 순환 불가능
        if total_gas < total_cost:
            return -1

        # 총 gas가 총 cost보다 크다면 무조건 순환 가능
        start_index = 0
        current_gas = 0

        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]

            # 현재 위치에서 다음 위치로 이동 불가능하면 다음 위치를 시작점으로 설정
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0

        # 루프가 끝까지 돌았을 때 start_index로 남은 값이 유일한 해답
        return start_index