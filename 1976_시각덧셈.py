#시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성

t = int(input())

for tc in range(1, t+1):
    time = list(map(int, input().split()))

    sum_hour = time[0] + time[2]
    sum_min = time[1] + time[3]

    if sum_min > 59:
        sum_min -= 60
        sum_hour += 1

    if sum_hour > 12:
        sum_hour -= 12

    print(f'#{tc} {sum_hour} {sum_min}')
