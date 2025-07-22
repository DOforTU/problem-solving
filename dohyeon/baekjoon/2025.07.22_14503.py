# 문제
# 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.
# https://www.acmicpc.net/problem/14503

# n x m 크기의 방이 주어지고, 로봇 청소기의 초기 위치와 방향이 주어진다.
# (r, c) 위치에서 d 방향을 바라보고 있는 로봇 청소기가 청소를 시작한다.
# d=0은 북쪽, 1은 동쪽, 2는 남쪽, 3은 서쪽을 의미한다.

# 1인 경우 벽, 0인 경우 청소가 되지 않은 빈 곳이다.
# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우, 
# 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다. 
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 
# 3-1. 반시계 방향으로 90도 회전한다.
# 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다. 
# 3-3. 1번으로 돌아간다.

n, m = map(int, input().split())
r, c, d = map(int, input().split())

# rooms = [[0] * m for _ in range(n)]

# for i in range(n):
#     temp = list(map(int, input().split()))
#     for j in range(m):
#         rooms[i][j] = temp[j]

# 위 방법대신 아래처럼 입력받을 수 있음.
rooms = [list(map(int, input().split())) for _ in range(n)]

# print("[DEBUG] Initial Room State:")
# for i in range(n):
#     print(rooms[i])

# 필요한 함수들 정의
# 1. 주변 4칸 탐색
def get_surrounding_positions(r, c):
    return [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]

# 2. 방향 회전(반시계 방향이므로 왼쪽 회전만 필요)
def turn_left(d):
    return (d - 1) % 4

# 3. 청소 상태 확인 및 청소
def clean(r, c):
    if rooms[r][c] == 0:  # 청소되지 않은 빈 칸
        rooms[r][c] = 2  # 청소 완료 상태로 변경
        return True
    return False

# 4. 후진: 후진 가능한지 true/false 반환
def can_move_back(r, c, d):
    if d == 0:  # 북쪽
        return r + 1 < n and rooms[r + 1][c] != 1
    elif d == 1:  # 동쪽
        return c - 1 >= 0 and rooms[r][c - 1] != 1
    elif d == 2:  # 남쪽
        return r - 1 >= 0 and rooms[r - 1][c] != 1
    elif d == 3:  # 서쪽
        return c + 1 < m and rooms[r][c + 1] != 1
    
# 5. 최종 코드
def robot_vacuum(r, c, d):
    cleaned_count = 0

    while True:
        # 현재 위치 청소
        if clean(r, c):
            cleaned_count += 1
        
        # 주변 4칸 탐색
        surrounding_positions = get_surrounding_positions(r, c)
        found_cleanable = False
        
        for i in range(4):
            new_d = turn_left(d)  # 반시계 방향으로 회전
            new_r, new_c = surrounding_positions[i]
            
            if 0 <= new_r < n and 0 <= new_c < m and rooms[new_r][new_c] == 0:
                r, c, d = new_r, new_c, new_d  # 이동
                found_cleanable = True
                break
        
        if not found_cleanable:  # 청소할 수 있는 칸이 없을 때
            if can_move_back(r, c, d):  # 후진 가능 여부 확인
                if d == 0:  # 북쪽
                    r += 1
                elif d == 1:  # 동쪽
                    c -= 1
                elif d == 2:  # 남쪽
                    r -= 1
                elif d == 3:  # 서쪽
                    c += 1
            else:
                break  # 후진 불가능하면 종료

    return cleaned_count

print(robot_vacuum(r, c, d))