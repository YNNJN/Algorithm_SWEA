#방에 적힌 숫자가 현재 방에 적힌 숫자보다 1 더 커야
#어떤 수가 적힌 방에서 출발해야 가장 많은 개수의 방을 이동할 수 있는지?
#이동 가능 방 개수 최대인 방이 여럿이라면 그 중 적힌 수 가장 작은 것 출력


#필요한 값을 계속 copy 해두는 방법으로 풀이
# ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for tc in range(int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     max_value = 0
#     result = n**2 + 1
#     for i in range(n):
#         for j in range(n):
#             s = arr[i][j]
#             cnt = 1
#             while True:
#                 for d in ds:
#                     nr = i + d[0]
#                     nc = j + d[1]
#                     if 0 <= nr < n and 0 <= nc < n:
#                         if arr[nr][nc] - arr[i][j] == 1:
#                             cnt += 1
#                             i,j = nr, nc
#                             break
#                 else:
#                     break
#             if max_value < cnt:
#                 max_value = cnt
#                 result = s
#             elif cnt == max_value and result > s:
#                 max_value = cnt
#                 result = s
#     print('#{} {} {}'.format(tc+1, result, max_value))



#충분한 배열을 만들어두고, 포문을 둘로 나눠 처리 -> 실행시간 1/2
for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [0] * ((n**2)+1)
    max_cnt = -1
    ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(n):
            for d in ds:
                nr = i + d[0]
                nc = j + d[1]
                if 0 <= nr < n and 0 <= nc < n:
                    if arr[nr][nc] - arr[i][j] == 1:
                        result[arr[i][j]] = 1
                        break

    for i in range(1, n**2):
        if result[i] == 1 and result[i-1] == 0:
            cnt = 1
            while True:
                if result[i+cnt] == 1:
                    cnt += 1
                else:
                    break

            if max_cnt < (cnt+1):
                max_cnt = cnt+1
                result_num = i
    print('#{} {} {}'.format(tc+1, result_num, max_cnt))
