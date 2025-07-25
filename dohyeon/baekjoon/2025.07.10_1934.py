# 문제
# 두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다. 이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다. 예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

# 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 둘째 줄부터 T개의 줄에 걸쳐서 A와 B가 주어진다. (1 ≤ A, B ≤ 45,000)

# 출력
# 첫째 줄부터 T개의 줄에 A와 B의 최소공배수를 입력받은 순서대로 한 줄에 하나씩 출력한다.

# LCM 최소공배수 (Least Common Multiple) - 시간이 오래걸림
def lcm(x, y):
    a = 1
    while a%x != 0 or a % y != 0: # => 같음 => a%x == 0 and a%y == 0 
        a += 1
    
    return a

# LCM 최소공배수 (Least Common Multiple) - 더 빠르지만, 그래도 오래걸림
def lcm_2(x, y): 
    multiple = max(x, y)
    while True:
        if multiple % x == 0 and multiple % y == 0:
            return multiple
        multiple += max(x, y)

# LCM 최소공배수 (Least Common Multiple) - 가장 빠름
def lcm_3(x, y):
    """ 최소공배수는 두 수의 곱을 최대공약수로 나눈 값이다. """
    return x * y // gcd(x, y)

# GCD 최대공약수 (Greatest Common Divisor)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm_3(a, b))