def bfs(si,sj):
    global cnt
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    q.append((si, sj))
    visited.append((si, sj))

    while q:
        si, sj = q.pop(0)
        for k in range(4):
            nr = si + dr[k]
            nc = sj + dc[k]
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if maze[nr][nc] == 1: continue
            if (nr,nc) not in visited:
                q.append((nr, nc))
                visited.append((nr, nc))
                cnt_list[nr][nc] = cnt_list[si][sj] + 1
                if maze[nr][nc] == 3:
                    cnt = cnt_list[nr][nc] - 1
                    return


for tc in range(int(input())):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = []

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                si, sj = i,j
                break

    cnt = 0
    cnt_list = [[0] * n for _ in range(n)]
    q = []
    bfs(si,sj)
    print('#{} {}'.format(tc+1, cnt))