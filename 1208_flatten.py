t = 10
m = 100  # 가로길이

for tc in range(1, t + 1):
    n = int(input())  # 덤프 횟수
    arr = list(map(int, input().split()))
    for i in range(n):  # 덤프 횟수만큼 반복
        min = 1000000
        max = 0
        max_idx = 0  # 최대값일 때의 위치 정보 저장
        min_idx = 0

        for j in range(m):
            if max < arr[j]:
                max = arr[j]  # 최고 상자 높이 갱신
                max_idx = j  # 최고 상자 높이의 위치 갱신
            if min > arr[j]:
                min = arr[j]
                min_idx = j

        # 덤핑하기
        arr[max_idx] -= 1
        arr[min_idx] += 1

    max = 0
    min = 100000000
    for i in range(m):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]

    ans = max - min
    print('#{} {}'.format(tc, ans))