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

# 방향 회전(반시계 방향이므로 왼쪽 회전만 필요)
# 방향: 북, 동, 남, 서
dr = [-1, 0, 1, 0] # 행(row) 방향으로의 변화량
dc = [0, 1, 0, -1] # 열(column) 방향으로의 변화량

def turn_left(d):
    return (d + 3) % 4  # 반시계 방향 회전

# 로봇 청소기 작동 함수
def robot_vacuum(r, c, d):
    cleaned_count = 0  # 청소한 칸의 수를 저장

    while True:
        # 1. 현재 칸이 아직 청소되지 않은 경우, 청소 수행
        if rooms[r][c] == 0:
            rooms[r][c] = 2  # 청소 완료 표시 (2)
            cleaned_count += 1

        cleaned = False  # 주변 청소 여부 확인용 플래그

        # 2. 주변 4칸 중 청소되지 않은 빈 칸이 있는지 탐색
        for _ in range(4):
            d = turn_left(d)  # 반시계 방향으로 회전
            nr = r + dr[d]    # 회전한 방향의 앞쪽 좌표
            nc = c + dc[d]

            # 그 칸이 청소되지 않은 빈 칸이라면
            if 0 <= nr < n and 0 <= nc < m and rooms[nr][nc] == 0:
                r, c = nr, nc  # 그 방향으로 한 칸 전진
                cleaned = True
                break  # 청소할 곳을 찾았으므로 더 이상 탐색하지 않음

        # 3. 네 방향 모두 청소할 곳이 없을 경우
        if not cleaned:
            back_dir = (d + 2) % 4  # 현재 방향 기준 뒤쪽 방향 계산
            br = r + dr[back_dir]   # 후진할 위치 계산
            bc = c + dc[back_dir]

            # 후진할 수 있다면
            if 0 <= br < n and 0 <= bc < m and rooms[br][bc] != 1:
                r, c = br, bc  # 후진하고 다시 반복
            else:
                break  # 뒤가 벽이면 작동 종료

    return cleaned_count  # 청소한 칸 수 반환


print(robot_vacuum(r, c, d))