# 몫과 나머지 출력하기

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split(' '))
    print(f'#{i} {int(a / b)} {a % b}')