# 2072. 홀수만 더하기
# 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성


t = int(input())

for i in range(1, t+1):
    l = map(int, input().split(' '))
    new_l = []

    for num in l:
        if num % 2:
            new_l.append(num)

    print(f'#{i} {sum(new_l)}')
