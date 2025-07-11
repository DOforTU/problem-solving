# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
# (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

m, n = map(int, input().split())

if n < 2:
    print("") # 2보다 작은 경우 소수는 없으므로 빈 줄 출력

# 소수 초기화
i = 2

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): # 제곱근까지만 검사
        if num % i == 0: # 나누어 떨어지면 소수 아님
            return False
    return True

while i <= n:
    if i >= m and is_prime(i):  # m 이상인 경우에만 출력
        print(i)
    i += 1