import collections
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        return self.leastInterval_sort(tasks, n)

    def leastInterval_math(self, tasks: List[str], n: int) -> int:
        # 1. 작업 빈도수 계산
        # 'A': 3, 'B': 2, ... 와 같이 딕셔너리 형태로 저장
        task_counts = collections.Counter(tasks)
        
        if not task_counts:
            return 0
        
        # 2. 최대 빈도수 (M) 찾기
        max_freq = max(task_counts.values()) # 예: 10
        
        # 3. 최대 빈도수와 같은 횟수를 가진 작업의 개수 (K) 찾기
        # 프레임워크의 마지막 덩어리를 채우는 데 사용
        max_freq_count = 0
        for count in task_counts.values():
            if count == max_freq:
                max_freq_count += 1 # 예: 'C'만 10개라면 K=1
                
        
        # 4. 쿨다운 기반 최소 시간 (프레임워크 길이) 계산
        # (M - 1) * (n + 1): M개의 작업을 n+1 간격으로 배치할 때 필요한 총 슬롯
        # + K: 마지막 덩어리에 들어가는 최대 빈도수 작업의 개수
        min_time_by_cooldown = (max_freq - 1) * (n + 1) + max_freq_count
        
        # 5. 최종 결과 반환
        # 전체 작업 수(len(tasks))와 쿨다운 기반 최소 시간(min_time_by_cooldown) 중
        # 더 긴 시간이 최소 소요 시간
        return max(min_time_by_cooldown, len(tasks))

    
    def leastInterval_sort(self, tasks: List[str], n: int) -> int:
        # 1. 딕셔너리({})를 사용해 작업 빈도수 계산
        task_counts = {}
        for task in tasks:
            task_counts[task] = task_counts.get(task, 0) + 1
        
        time = 0
        
        # 2. 시뮬레이션 시작: 남은 작업이 있을 때까지 반복
        while task_counts:
            # 2-1. 현재 남아있는 작업을 빈도수 기준으로 내림차순 정렬
            # [('A', 3), ('B', 3)] 형태로 정렬됨
            sorted_tasks = sorted(task_counts.items(), key=lambda item: item[1], reverse=True)
            
            # 2-2. 이번 n+1 주기 동안 실행할 작업 목록을 임시로 저장
            executed_in_cycle = [] 
            
            # n+1 간격 동안 작업 수행 시도
            for i in range(n + 1):
                # 쿨다운 주기(n+1) 내에서 실행할 작업이 있다면
                if i < len(sorted_tasks):
                    task_name = sorted_tasks[i][0]
                    executed_in_cycle.append(task_name)
                
                # 실행할 작업이 더 이상 없더라도,
                # 쿨다운 간격이 아직 끝나지 않았고 (i < n+1),
                # 남아있는 작업이 있다면 Idle 시간을 추가해야 함.
                # 단, 이 if 문은 쿨다운 간격(n+1)까지만 실행되므로 별도로 Idle을 명시하지 않고,
                # 전체 시간 계산에 반영
            
            # 2-3. 작업 횟수 감소 및 제거
            for task_name in executed_in_cycle:
                task_counts[task_name] -= 1
                if task_counts[task_name] == 0:
                    del task_counts[task_name]
            
            # 2-4. 시간 계산
            
            # 아직 작업이 남아있다면, 이번 주기는 n+1 전체를 소요 (Idle 포함)
            if task_counts:
                time += (n + 1)
            # 남아있는 작업이 없다면 (마지막 주기),
            # 실제로 실행된 작업 개수(len(executed_in_cycle))만큼만 시간을 더함.
            else:
                time += len(executed_in_cycle)
                
        return time

    def leastInterval_heap(self, tasks: List[str], n: int) -> int:
        # 1. 빈도수 계산
        counts = collections.Counter(tasks)
        print(counts)
        
        # 2. 최대 힙 초기화
        # heapq는 최소 힙이므로, 최대 힙처럼 사용하기 위해 횟수에 음수를 붙여서 저장.
        # 예: 빈도수 3 -> -3 저장
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        print(max_heap)
        
        time = 0 # 전체 소요 시간
        
        # 3. 시뮬레이션 루프 실행 (힙이 빌 때까지)
        while max_heap:
            cycle_time = 0 # 이번 주기에 실제로 실행된 작업/idle 수
            temp = []      # 쿨다운이 필요한 작업 임시 저장소
            
            # n+1 간격(쿨다운 주기) 동안 작업 수행 시도
            for _ in range(n + 1):
                if max_heap:
                    # 3-1. 가장 빈번한 작업 꺼내기 (가장 작은 음수)
                    count = heapq.heappop(max_heap) 
                    
                    # 3-2. 횟수 감소 및 임시 저장
                    count += 1 # 음수이므로 +1은 실제 횟수 -1과 같음
                    
                    if count < 0:
                        temp.append(count) # 남은 횟수가 있으면 (0이 아니면) 임시 저장
                    
                    cycle_time += 1 # 작업 실행
                
                # 힙이 비었더라도 쿨다운 간격(n+1)이 끝나지 않았다면 Idle 시간으로 간주
                elif temp:
                    # 힙이 비었더라도, 아직 n+1 사이클이 끝나지 않았으면 Idle 시간을 추가
                    cycle_time += 1
                
                # 힙도 비었고, n+1 사이클도 끝났다면 루프 종료
                else:
                    break 
                    
            # 4. 전체 시간 업데이트
            # 힙에 남아있는 작업이 있다면, 현재 주기는 n+1의 전체 길이로 계산
            if max_heap or temp:
                time += (n + 1)
            # 힙이 완전히 비었다면, 현재 주기는 cycle_time (실제 작업 횟수)으로 계산하고 종료
            else:
                time += cycle_time
                break # 종료 조건
                
            # 5. 다음 주기를 위해 임시 작업들을 힙에 다시 넣기
            for item in temp:
                heapq.heappush(max_heap, item)
                
        return time