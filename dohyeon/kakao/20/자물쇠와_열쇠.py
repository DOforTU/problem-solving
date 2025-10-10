def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    # 1. 자물쇠 확장 (Padded Lock 생성)
    # 새로운 크기: N + 2 * (M - 1)
    # 열쇠가 자물쇠를 완전히 덮을 수 있는 영역
    extended_size = N + 2 * (M - 1)
    
    # lock 배열을 중앙에 배치: 0인 패딩을 만드는 과정(중앙은 기존 lock과 동일)
    extended_lock = [[0] * extended_size for _ in range(extended_size)]
    for i in range(N):
        for j in range(N):
            extended_lock[i + M - 1][j + M - 1] = lock[i][j]

    # 2. 모든 회전 (0, 90, 180, 270도) 검사
    rotated_key = key
    for _ in range(4): # 4번 회전
        rotated_key = rotate(rotated_key, clock=True) # 90도 시계 방향 회전
        
        # 3. 모든 이동 위치 검사
        # 열쇠의 좌상단 좌표 (r, c)를 extended_lock 위에서 이동
        # 이동 범위: (0, 0)부터 (extended_size - M, extended_size - M)까지
        for r in range(extended_size - M + 1):
            for c in range(extended_size - M + 1):
                
                # 4. 열쇠 삽입 시뮬레이션
                temp_lock = [row[:] for row in extended_lock] # 임시 배열 복사
                is_collision = False
                
                # 열쇠를 겹쳐보고 돌기 충돌 여부 확인
                for i in range(M):
                    for j in range(M):
                        # 열쇠의 돌기(1)와 자물쇠의 돌기(1)가 만나면 충돌 (합이 2)
                        if rotated_key[i][j] == 1 and extended_lock[r + i][c + j] == 1:
                            is_collision = True
                            break
                        # 열쇠 삽입
                        temp_lock[r + i][c + j] += rotated_key[i][j]
                    if is_collision:
                        break
                
                # 5. 자물쇠 열림 조건 확인
                if not is_collision and check(temp_lock, N, M):
                    return True # 자물쇠가 열렸다면 즉시 True 반환

    return False # 모든 경우를 검사했지만 열 수 없다면 False 반환

def rotate(key, clock=True):
    """clock=true라면 시계 방향으로 회전, false는 반시계"""
    new_key = []
    if clock: # 시계 방향일 경우
        # 각 요소의 첫번째 요소가 거꾸로 new_key의 첫 행이 됨.
        for i in range(len(key)):
            temp = []
            for j in range(len(key)-1, -1, -1):
                temp.append(key[j][i])
            new_key.append(temp)
        return new_key
    else: # 반시계라면
        for i in range(len(key)-1, -1, -1):
            temp = []
            for j in range(len(key)):
                temp.append(key[j][i])
            new_key.append(temp)
        return new_key
        

def check(new_lock, N, M):
    # 중앙 N x N 영역만 검사
    for i in range(M - 1, M - 1 + N):
        for j in range(M - 1, M - 1 + N):
            # 1이 아닌 칸(즉, 0이나 2인 칸)이 있으면 실패
            if new_lock[i][j] != 1: 
                return False
    return True

# TEST
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))