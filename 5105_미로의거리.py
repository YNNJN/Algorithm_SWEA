#최소 몇 개의 칸을 지나야 출발지에서 도착지에 다다를 수 있는지
def find(i, j):
    global cnt
    q = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    s = [[i, j, q]]
    while s:
        [pi, pj, q] = s.pop()
        for k in range(4):
            nr = pi + dr[k]
            nc = pj + dc[k]
            if nr < 0 or nr >= n or nc < 0 or nc >= n: continue
            if maze[nr][nc] == 1: continue
            if maze[nr][nc] == 3:
                cnt.append(q)
                break
            if maze[nr][nc] == 5: continue
            maze[pi][pj] = 5
            q += 1
            s.append([nr, nc, q])
            q -= 1
    return


for tc in range(int(input())):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    cnt = []

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                si, sj = i, j
                break
    find(si, sj)
    if len(cnt) != 0:
        print('#{} {}'.format(tc+1, min(cnt)))
    else:
        print('#{} {}'.format(tc+1, 0))