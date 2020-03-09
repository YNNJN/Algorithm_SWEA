def dfs(r,c,cut,leng): #좌표, 남은 깎음 횟수, 등산로 길이
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    global max_value
    if max_value < leng:
        max_value = leng
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if arr[r][c] > arr[nr][nc]:
                dfs(nr, nc, cut, leng+1) #주변의 낮은 칸으로 이동
            elif visited[nr][nc] == 0 and cut > 0 and arr[r][c] > arr[nr][nc] - k:
                origin = arr[nr][nc] #카피
                arr[nr][nc] = arr[r][c] - 1 #주변 칸을 깎아서 이동
                dfs(nr, nc, 0, leng+1)
                arr[nr][nc] = origin #높이 원상복구
    visited[r][c] = 0

for tc in range(int(input())):
    n,k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    h = 0
    for i in range(n):
        for j in range(n):
            if h < arr[i][j]:
                h = arr[i][j]
    max_value = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == h:
                dfs(i, j, 1, 1)

    print('#{} {}'.format(tc+1, max_value))



