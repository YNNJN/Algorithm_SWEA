# 밭에 놓을 수 있는 콩의 최대 개수
for tc in range(int(input())):
    n,m = map(int, input().split())
    beans = [[1 for _ in range(n)] for _ in range(m)]
    cnt = n * m
    for i in range(m):
        for j in range(n):
            if beans[i][j]:
                if i + 2 < m and beans[i+2][j]:
                    beans[i+2][j] = 0
                    cnt -= 1
                if j + 2 < n and beans[i][j+2]:
                    beans[i][j+2] = 0
                    cnt -= 1
    print('#{} {}'.format(tc+1, cnt))